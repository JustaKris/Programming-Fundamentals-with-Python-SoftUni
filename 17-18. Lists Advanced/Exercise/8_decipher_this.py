def decipher(words: list) -> list:
    deciphered_words = []

    for word in words:
        code = int(''.join(filter(str.isdigit, word)))
        word = word.replace(str(code), chr(code))
        deciphered_word = word[0] + word[-1] + word[2:-1] + word[1]
        deciphered_words.append(deciphered_word)

    return deciphered_words


secret_message = input().split()
print(" ".join(decipher(secret_message)))
