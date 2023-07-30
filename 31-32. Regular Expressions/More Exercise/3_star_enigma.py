import re

number_of_messages = int(input())


planets = {}
for _ in range(number_of_messages):
    encrypted_message = input()

    decryption_key = 0
    for letter in encrypted_message:
        if letter.lower() in ['s', 't', 'a', 'r']:
            decryption_key += 1
    # print(decryption_key)

    decrypted_message = ""
    for letter in encrypted_message:
        decrypted_letter = chr(ord(letter) - decryption_key)
        decrypted_message += decrypted_letter
    # print(decrypted_message)

    # pattern = r'@(?P<planet_name>[A-Z][a-z]+).+:(?P<population>\d+)!(?P<attack_type>[AD]{1})!->(?P<soldier_count>\d+)'
    pattern = r'@(?P<planet_name>[A-Z][a-z]+).{,50}:(?P<population>\d+).{,50}!(?P<attack_type>[AD]{1})!' \
              r'.{,50}->(?P<soldier_count>\d+)'
    matches = re.finditer(pattern, decrypted_message)
    for match in matches:
        planet = match.groupdict()['planet_name']
        # print(planet)
        population = int(match.groupdict()['population'])
        # print(population)
        attack_type = match.groupdict()['attack_type']
        # print(attack_type)
        soldier_count = int(match.groupdict()['soldier_count'])
        # print(soldier_count)
        planets[planet] = {'population': population, 'attack_type': attack_type, 'soldier_count': soldier_count}

# planets = sorted(planets)
myKeys = list(planets.keys())
myKeys.sort()
planets = {i: planets[i] for i in myKeys}
# print(planets)

attacked_planets = len([planet for planet, info in planets.items() if info['attack_type'] == 'A'])
destroyed_planets = len(planets.keys()) - attacked_planets

print(f"Attacked planets: {attacked_planets}")
for planet, info in planets.items():
    if info["attack_type"] == "A":
        print(f"-> {planet}")

print(f"Destroyed planets: {destroyed_planets}")
for planet, info in planets.items():
    if info["attack_type"] == "D":
        print(f"-> {planet}")
