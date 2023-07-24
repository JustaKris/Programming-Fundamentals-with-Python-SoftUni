import re


def process_order(order):
    pattern = r"%([A-Z][a-z]+)%<([\w]+)>\|(\d+)\|([\d.]+)\$"
    match = re.match(pattern, order)

    if match:
        customer = match.group(1)
        product = match.group(2)
        count = int(match.group(3))
        price = float(match.group(4))
        total_price = count * price
        return f"{customer}: {product} - {total_price:.2f}"

    return None


def main():
    orders = []
    total_income = 0.0

    while True:
        line = input()
        if line == "end of shift":
            break

        order_result = process_order(line)
        if order_result:
            orders.append(order_result)
            total_income += float(re.search(r"\d+\.\d+", line).group())

    for order in orders:
        print(order)

    print(f"Total income: {total_income:.2f}")


if __name__ == "__main__":
    main()
