import re


def collect_food_info(string):
    supplies = {}
    total_calories = 0

    # patterns = r"(\#|\|)([A-Za-z\s]+)(\1)(\d{2}\/\d{2}\/\d{2})(\1)(\d{1,5})(\1)"
    # foods = re.findall(patterns, string)

    # for food in foods:
    #     supplies[food[1]] = {"expiration_date": food[2], "calories": int(food[3])}
    #     total_calories += int(food[3])

    pattern = r"(\#|\|)(?P<food>[A-Za-z\s]+)(\1)(?P<date>\d{2}\/\d{2}\/\d{2})(\1)(?P<calories>\d{1,5})(\1)"
    matches = re.finditer(pattern, string)

    for match in matches:
        item = match.groupdict()
        supplies[item["food"]] = {"expiration_date": item["date"], "calories": item["calories"]}
        total_calories += int(item["calories"])

    return supplies, total_calories


# Reading text string input containing food information
text = input()

# Extracting required information from string
supplies, total_calories = collect_food_info(text)
days_worth_of_supplies = total_calories // 2000

# Printouts
print(f"You have food to last you for: {days_worth_of_supplies} days!")
for food, details in supplies.items():
    print(f"Item: {food}, Best before: {details['expiration_date']}, Nutrition: {details['calories']}")
