#função que encripta uma palavra "message" consoante o numero de "offset" escolhido do abcedario
def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = '' #nova mensagem encriptada vazia

    for char in message.lower():
        if char == ' ': #se a palavra tiver um epaço
            encrypted_text += char #adiciona espaço à mensagem encriptada
        else:
            index = alphabet.find(char) #adiciona ao index a posição da letra da "message" segundo o abcedario
            new_index = (index + offset) % len(alphabet) #novo index com a soma do offset escolhido
            encrypted_text += alphabet[new_index] #adicina à mensagem encriptada a letra do alfabeto correspondente ao novo index
    print('plain text:', message)
    print('encrypted text:', encrypted_text)