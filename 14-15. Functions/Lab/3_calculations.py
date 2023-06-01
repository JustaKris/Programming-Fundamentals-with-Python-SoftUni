def calculate(operator, num_1, num_2):
    if operator == "multiply":
        return num_1 ** num_2
    elif operator == "divide":
        return num_1 // num_2
    elif operator == "add":
        return num_1 + num_2
    elif operator == "subtract":
        return num_1 - num_2
    else:
        raise Exception("Invalid operator")


input_operator = input()
input_num_1 = int(input())
input_num_2 = int(input())

print(calculate(input_operator, input_num_1, input_num_2))


# Approach 2
def calculate2(operator, num_1, num_2):
    return {
        "multiply": num_1 * num_2,
        "divide": num_1 / num_2,
        "add": num_1 + num_2,
        "subtract": num_1 - num_2
    }.get(operator, "Invalid operator")
