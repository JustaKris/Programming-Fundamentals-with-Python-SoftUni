events = input().split("|")

energy = 100
coins = 100
factory_is_open = True

for event in events:
    action_or_ingredient, value = event.split("-")
    value = int(value)
    if action_or_ingredient == 'rest':
        gained_energy = min(value, 100 - energy)
        energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif action_or_ingredient == 'order':
        if energy >= 30:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= value:
            coins -= value
            print(f"You bought {action_or_ingredient}.")
        else:
            print(f"Closed! Cannot afford {action_or_ingredient}.")
            factory_is_open = False
            break

if factory_is_open:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
