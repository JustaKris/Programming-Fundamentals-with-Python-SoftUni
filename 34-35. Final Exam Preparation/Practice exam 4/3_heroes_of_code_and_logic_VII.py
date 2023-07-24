def cast_spell(heroes, hero_name, mp_required, spell):
    if heroes[hero_name]['mp'] >= mp_required:
        heroes[hero_name]['mp'] -= mp_required
        print(f"{hero_name} has successfully cast {spell} and now has {heroes[hero_name]['mp']} MP!")
    else:
        print(f"{hero_name} does not have enough MP to cast {spell}!")
    return heroes


def take_damage(heroes, hero_name, damage, attacker):
    if heroes[hero_name]['hp'] > damage:
        heroes[hero_name]['hp'] -= damage
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['hp']} HP left!")
    else:
        del heroes[hero_name]
        print(f"{hero_name} has been killed by {attacker}!")
    return heroes


def recharge(heroes, hero_name, amount):
    starting_mp = heroes[hero_name]['mp']
    heroes[hero_name]['mp'] += amount
    if heroes[hero_name]['mp'] > 200:
        amount = 200 - starting_mp
        heroes[hero_name]['mp'] = 200
    print(f"{hero_name} recharged for {amount} MP!")
    return heroes


def heal(heroes, hero_name, amount):
    starting_hp = heroes[hero_name]['hp']
    heroes[hero_name]['hp'] += amount
    if heroes[hero_name]['hp'] > 100:
        amount = 100 - starting_hp
        heroes[hero_name]['hp'] = 100
    print(f"{hero_name} healed for {amount} HP!")
    return heroes


# Reading inputs and setting up the heroes dictionary
number_of_heroes = int(input())
heroes = {}
for _ in range(number_of_heroes):
    hero_name, hp, mp = input().split()
    heroes[hero_name] = {'hp': int(hp), 'mp': int(mp)}

# Logic loop for incoming actions
while True:
    command, *params = input().split(" - ")

    if command == 'End':
        break

    if command == 'CastSpell':
        hero_name, mp_required, spell = params
        mp_required = int(mp_required)
        heroes = cast_spell(heroes, hero_name, mp_required, spell)

    elif command == 'TakeDamage':
        hero_name, damage, attacker = params
        damage = int(damage)
        heroes = take_damage(heroes, hero_name, damage, attacker)

    elif command == 'Recharge':
        hero_name, amount = params
        amount = int(amount)
        heroes = recharge(heroes, hero_name, amount)

    elif command == "Heal":
        hero_name, amount = params
        amount = int(amount)
        heroes = heal(heroes, hero_name, amount)

# Final printouts
for hero, stats in heroes.items():
    print(f"{hero}\n  HP: {stats['hp']}\n  MP: {stats['mp']}")
