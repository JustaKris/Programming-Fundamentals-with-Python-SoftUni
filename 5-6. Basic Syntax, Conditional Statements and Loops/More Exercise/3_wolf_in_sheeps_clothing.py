# animals = 'wolf, sheep, sheep, sheep, sheep, sheep'

animals = str(input())

animals_list = animals.split(', ')

# print(animals_list)
index = len(animals_list) - 1
if animals_list[index] == 'wolf':
    print("Please go away and stop eating my sheep")
else:
    counter = 0
    for animal in animals_list[::-1]:
        if animal != 'wolf':
            # index -= 1
            counter += 1
        else:
            print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")

