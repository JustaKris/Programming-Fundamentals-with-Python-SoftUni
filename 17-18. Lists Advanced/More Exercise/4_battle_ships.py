field_rows = int(input())
field = []
for i in range(field_rows):
    current_row = [int(position) for position in input().split()]
    field.append(current_row)
attacks = input().split()

ships_destroyed = 0
for attack in attacks:
    current_attack = attack.split("-")
    attack_row = int(current_attack[0])
    attack_col = int(current_attack[1])
    if field[attack_row][attack_col] > 0:
        field[attack_row][attack_col] -= 1
        if field[attack_row][attack_col] == 0:
            ships_destroyed += 1

print(ships_destroyed)
