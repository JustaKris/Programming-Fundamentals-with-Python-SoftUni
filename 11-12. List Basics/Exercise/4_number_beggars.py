integers = input().split(", ")
integers = [int(integer) for integer in integers]
number_of_beggars = int(input())

beggars_sum = [0 for i in range(number_of_beggars)]

counter = 0
for i in range(len(integers)):
    if i > 0 and i % number_of_beggars == 0:
        counter += number_of_beggars
        beggars_sum[i - counter] += integers[i]
    else:
        beggars_sum[i - counter] += integers[i]
print(beggars_sum)


# ChatGPT solution
# numbers = input().split(", ")
# beggars_count = int(input())
#
# beggars = [0] * beggars_count
#
# for i in range(len(numbers)):
#     number = int(numbers[i])
#     beggar_index = i % beggars_count
#     beggars[beggar_index] += number
#
# print(beggars)
