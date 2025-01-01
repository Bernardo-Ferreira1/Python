def arithmetic_arranger(problems, show_answers=False):
    string=''
    primeiro=[]
    segundo=[]
    linhas=[]
    resultado1=[]
    index=-1
    if len(problems) > 5:
        return 'Error: Too many problems.'
    else:
        for i in problems:
            index+=1
            l_s=i.split()
            num1, operator, num2=l_s[0],l_s[1],l_s[2]
   
            if (num1.isnumeric()!=True or num2.isnumeric())!=True:
                return 'Error: Numbers must only contain digits.'

            if (len(num1)>4 or len(num2)) > 4:
                return 'Error: Numbers cannot be more than four digits.'

            if operator=='+':
                resultado=int(num1)+int(num2)
            elif l_s[1]=='-':
                resultado=int(num1)-int(num2)
            else:
                return "Error: Operator must be '+' or '-'."
            Nlinhas=(max(len(num1), len(num2)) + 2)
            primeiro.append(num1.rjust(Nlinhas))
            segundo.append(operator+ ' '+ num2.rjust(Nlinhas -2))
            
            linhas.append('-'* Nlinhas)
            resultado1.append(str(resultado).rjust(Nlinhas))
            string='    '.join(primeiro) + '\n' + '    '.join(segundo) + '\n' + '    '.join(linhas)
            if show_answers:
                string += '\n' + '    '.join(resultado1)
        return string

            
print(f'\n{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])}')