def encrypt_text(text):

    encrypted_text = ""

    for symbol in text:
        encrypted_symbol = chr(ord(symbol) + 3)
        encrypted_text += encrypted_symbol
    return encrypted_text


text = input()

print(encrypt_text(text))
