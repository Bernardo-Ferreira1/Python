def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1] #inverte a ordem
    odd_digits = card_number_reversed[::2] #grava os numeros na posição impar

    for digit in odd_digits:
        sum_of_odd_digits += int(digit) #soma os numeros na posição impar

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2] #grava os numeros na posição par
    for digit in even_digits:
        number = int(digit) * 2 #multiplica por 2 os numeros na posição par
        if number >= 10:
            number = (number // 10) + (number % 10) #se essa multiplicação for >10, soma os doi digitos
        sum_of_even_digits += number #soma os numeros na posição par
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0 #se o total fôr multiplo de 10, retorna True

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''}) #retira os sinais e espaços
    translated_card_number = card_number.translate(card_translation)#nova string sem os sinais

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()