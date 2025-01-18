def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():

        # Append space to the message
        if not char.isalpha(): #se não for uma letra (um espaço) adiciona logo à mensagem final
            encrypted_text += char
        else:
            # Find the right key character to encode
            key_char = key[key_index % len(key)] #key_char= à letra na posição key_index da palavra key
            key_index += 1 #incrementa 1 para passar à próxima letra da key

            # Define the offset and the encrypted letter
            offset = alphabet.index(key_char) #vai buscar a posição no abcedario consoante a posição da letra da key a ser utilizada
            index = alphabet.find(char) #adiciona ao index a posição da letra da "message" segundo o abcedario
            new_index = (index + offset*direction) % len(alphabet) #novo index com a soma do offset escolhido
            encrypted_text += alphabet[new_index] #adicina à mensagem encriptada a letra do alfabeto correspondente ao novo index
#vais buscar a posição de cada letra da message (index) e a posição de cada letra da key(offset) e soma os dois
    return encrypted_text

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

#print(f'\nEncrypted text: {text}')
#print(f'Key: {custom_key}')
#decryption = decrypt(text, custom_key)
#print(f'\nDecrypted text: {decryption}\n')