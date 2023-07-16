import pyotp


def generate_secret_key():
    secret_key = pyotp.random_base32()
    return secret_key


# Generate OTP for the user
def generate_otp(secret_key):
    # Create a TOTP with the secret key
    totp = pyotp.TOTP(secret_key)

    # Generate OTP
    otp = totp.now()
    return otp


# Verify OTP entered by the user
def verify_otp(secret_key, entered_otp):
    totp = pyotp.TOTP(secret_key)

    return totp.verify(entered_otp)


secret_key = generate_secret_key()
otp = generate_otp(secret_key)

# Display the generated OTP
print("Generated OTP:", otp)
print()

# Prompt the user to enter OTP
entered_otp = input("Enter the OTP: ")

if verify_otp(secret_key, entered_otp):
    print("OTP verification successful!")
