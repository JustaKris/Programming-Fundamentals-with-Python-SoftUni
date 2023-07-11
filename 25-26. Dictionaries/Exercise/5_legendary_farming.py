key_materials = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}
legendary_items = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"
}

junk_items = {}

obtained_item = ""

while True:
    line = input().lower()
    materials = line.split()

    for i in range(0, len(materials), 2):
        quantity = int(materials[i])
        material = materials[i + 1]

        if material in key_materials:
            key_materials[material] += quantity

            if key_materials[material] >= 250:
                obtained_item = legendary_items[material]
                key_materials[material] -= 250
                break
        else:
            if material not in junk_items:
                junk_items[material] = 0
            junk_items[material] += quantity

    if obtained_item != "":
        break

print(f"{obtained_item.capitalize()} obtained!")
print(f"shards: {key_materials['shards']}")
print(f"fragments: {key_materials['fragments']}")
print(f"motes: {key_materials['motes']}")

for item, count in junk_items.items():
    print(f"{item}: {count}")
