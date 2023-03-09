plain_sentence = input()
secret_code = input() 

def generate_cipher(plain_sentence):
cipher = {}
for i in range(len(plain_sentence)):
    if plain_sentence[i] != ' ' and plain_sentence[i] not in cipher:
    cipher[plain_sentence[i]] = chr(ord('a') + len(cipher))
    return cipher

def encrypt_code(secret_code, cipher):
    encrypted_code = ''
    for i in range(len(secret_code)):
        if secret_code[i] in cipher:
        encrypted_code += cipher[secret_code[i]]
        return encrypted_code

def encrypt(plain_sentence, secret_code):
    cipher = generate_cipher(plain_sentence[::-1])
    encrypted_code = encrypt_code(secret_code, cipher)
    return encrypted_code



encrypted_code = encrypt(plain_sentence, secret_code)

print(encrypted_code)