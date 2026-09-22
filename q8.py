import random

digits = int(input("Enter number of digits (4 or 6): "))

if digits == 4 or digits == 6:
    otp = random.randint(10 ** (digits - 1), 10 ** digits - 1)
    print("Generated OTP:", otp)
else:
    print("Please enter only 4 or 6.")