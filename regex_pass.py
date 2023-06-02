import re

while True:
    password = str(input("Enter your password(one upper,one lower,and one number at least),q to exit: "))
    check_pass = re.fullmatch(r"[A-Za-z0-9]{8,}", password)
    if password:
        if check_pass:
            print("Password is valid.")
        else:
            print("Password is invalid!")
    elif "q":
        break
