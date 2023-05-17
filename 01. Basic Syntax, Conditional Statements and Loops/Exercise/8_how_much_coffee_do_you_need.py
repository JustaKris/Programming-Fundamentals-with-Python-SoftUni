command = str(input())

things = ['coding', 'dog', 'cat', 'movie']
coffee_required = 0
while command != 'END':
    coffee_per_action = 0
    if command.lower() in things:
        if command == command.upper():
            coffee_per_action = 2
        else:
            coffee_per_action = 1
    coffee_required += coffee_per_action
    command = str(input())
if coffee_required > 5:
    print('You need extra sleep')
else:
    print(coffee_required)

