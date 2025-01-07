def add_time(start, duration,week_days=None):
    days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    tempo=start.split()[0] #as horas do start (string)
    tempo2=tempo.split(':')#retorna os start separadas []
    fuso=start.split()[1]#retorna AM e PM string
    if fuso=='PM': #torna o start no formato de 24h
        horas_24h=int(tempo2[0])+12
    else:
        horas_24h=int(tempo2[0])
    tempo_minutos=horas_24h*60+int(tempo2[1]) #dá o start em minutos
    duration_list=duration.split(':') #retorna a duration separado []
    duration_minutes=int(duration_list[0])*60+int(duration_list[1]) #retorna a duração em minutos
    new_time=tempo_minutos+duration_minutes #dá o tempo final em minutos

    if week_days!=None:
        index = next((i for i, day in enumerate(days)   if day.lower() == week_days.lower()), None) #devolve o indice a lista days do week_days introduzido
        resto=new_time//1440 #dá os dias que passaram
        if resto==1:
            next_day='(next day)'
            new_index = (index + resto) % len(days)
            string_day=days[new_index]
        elif resto>1:
            days_passed=resto
            new_index = (index + resto) % len(days) #novo indice adicionando o indice da lista days atual e incrementando os dias que passaram
            string_day=days[new_index] #devolve o novo dia
        elif resto==0:
            string_day=days[index]
    else:
        resto=new_time//1440
        string_day=''
        if resto==1:
            next_day='(next day)'

    new_time_AMPM_minutosTotal=new_time-1440*resto #Minutos totais a serem convertidos para AM PM
    new_time_AMPM_horas = new_time_AMPM_minutosTotal//60 #Retorna as horas em AMPM
    new_time_AMPM_minutos=new_time_AMPM_minutosTotal%60 #Retorna os minutos em AM PM
    
    if new_time_AMPM_horas == 0:
        new_time_AMPM_horas = 12
        AMPM = 'AM'
    elif new_time_AMPM_horas == 12:
        AMPM = 'PM'
    elif new_time_AMPM_horas > 12:
        new_time_AMPM_horas -= 12
        AMPM = 'PM'
    else:
        AMPM = 'AM'
    if week_days==None:
        if resto==0:    
            final_string=f'{new_time_AMPM_horas}:{new_time_AMPM_minutos:02} {AMPM}'
        elif resto==1:
            final_string=f'{new_time_AMPM_horas}:{new_time_AMPM_minutos:02} {AMPM} {next_day}'
        elif resto>1:
            final_string=f'{new_time_AMPM_horas}:{new_time_AMPM_minutos:02} {AMPM} ({resto} days later)'
    else:
        if resto==0:
            final_string=f'{new_time_AMPM_horas}:{new_time_AMPM_minutos:02} {AMPM}, {string_day}'
        elif resto==1:
           final_string=f'{new_time_AMPM_horas}:{new_time_AMPM_minutos:02} {AMPM}, {string_day} {next_day}' 
        elif resto>1:
           final_string=f'{new_time_AMPM_horas}:{new_time_AMPM_minutos:02} {AMPM}, {string_day} ({resto} days later)' 
    
#passar de 24h para 10:12

    
    return final_string
add_time('11:55 AM', '00:05')


#index = next((i for i, day in enumerate(days) if day.lower() == week_days.lower()), None)
"""Explanation:
day.lower() converts each element in the list to lowercase.
string.lower() converts the input string to lowercase as well.
enumerate(days) gives you both the index i and the corresponding element day in the list.
The next() function is used to find the first match and return the index. If no match is found, it will return None."""

