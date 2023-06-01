fires = input().split("#")
water = int(input())

effort = 0
total_fire = 0
cells_put_out = []

for fire in fires:
    fire_type, value = fire.split(" = ")
    value = int(value)

    if fire_type == "High" and not 81 <= value <= 125:
        continue
    elif fire_type == "Medium" and not 51 <= value <= 80:
        continue
    elif fire_type == "Low" and not 1 <= value <= 50:
        continue

    if water >= value:
        water -= value
        cells_put_out.append(value)
        effort += value * 0.25
        total_fire += value

print("Cells:")
for cell in cells_put_out:
    print(f"- {cell}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")