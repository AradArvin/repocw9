import re

password = str(input("Enter your password(one upper,one lower,and one number at least): "))

check_pass = re.fullmatch(r"[A-Za-z0-9]{8,}", password)

if check_pass:
    print("Password is valid.")
else:
    print("Password is invalid!")
