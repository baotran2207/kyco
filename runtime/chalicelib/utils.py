import math
import random
import secrets
import string


def generate_new_password(password_length=8) -> str:
    return "".join(
        (
            secrets.choice(string.ascii_letters + string.digits + string.punctuation)
            for i in range(password_length)
        )
    )


def generate_otp():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]

    return OTP
