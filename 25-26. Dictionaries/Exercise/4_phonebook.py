contact = input()

contacts = {}
while not contact.isdigit():
    name, phone_number = contact.split("-")
    contacts[name] = phone_number

    contact = input()

else:
    for _ in range(int(contact)):
        name_to_search = input()

        if name_to_search in contacts.keys():
            print(f"{name_to_search} -> {contacts[name_to_search]}")
        else:
            print(f"Contact {name_to_search} does not exist.")
