import re

num_inputs = int(input())
pattern = r"\|([A-Z]{4,})\|:#([A-Za-z]+ [A-Za-z]+)#"

for _ in range(num_inputs):
    line = input()
    matches = re.findall(pattern, line)
    if matches:
        boss_name = matches[0][0]
        boss_title = matches[0][1]
        strength = len(boss_name)
        armor = len(boss_title)
        print(f"{boss_name}, The {boss_title}")
        print(f">> Strength: {strength}")
        print(f">> Armor: {armor}")
    else:
        print("Access denied!")
