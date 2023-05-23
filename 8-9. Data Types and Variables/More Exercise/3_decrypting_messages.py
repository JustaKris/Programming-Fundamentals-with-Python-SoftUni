key = int(input())
number_of_inputs = int(input())

message = ""
for i in range(number_of_inputs):
    letter = str(input())
    decrypted_letter = chr(ord(letter) + key)
    message += decrypted_letter
print(message)
