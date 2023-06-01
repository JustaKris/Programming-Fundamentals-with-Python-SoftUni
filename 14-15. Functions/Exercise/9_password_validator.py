def password_validation(password):
    if len(password) not in range(6, 11):
        print("Password must be between 6 and 10 characters")
        return False

    if not password.isalnum():
        print("Password must consist only of letters and digits")
        return False

    digit_count = sum(char.isdigit() for char in password)
    if digit_count < 2:
        print("Password must have at least 2 digits")
        return False

    return True


password = input()
if password_validation(password):
    print("Password is valid")