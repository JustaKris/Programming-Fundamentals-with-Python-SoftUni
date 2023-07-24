import re


def validate_barcode(barcode):
    pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"
    if re.fullmatch(pattern, barcode):
        digits = re.findall(r"\d", barcode)
        return "".join(digits) if digits else "00"
    else:
        return False


number_of_barcodes = int(input())

for _ in range(number_of_barcodes):
    barcode = input()
    valid_barcode = validate_barcode(barcode)
    if valid_barcode:
        print(f"Product group: {valid_barcode}")
    else:
        print("Invalid barcode")
