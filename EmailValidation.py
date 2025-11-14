import re

class InvalidEmail(Exception):
    pass  # custom exception class

email = input("Enter Your Email ID: ")

reg = r'^[a-z0-9A-Z]+[._]?[a-z0-9A-Z]+[@]\w+[.]\w+$'

try:
    if not re.match(reg, email):
        raise InvalidEmail("Invalid Email ID")
    else:
        print("Valid email")
except InvalidEmail as e:
    print(e)
except:
    print("Check the email that you have entered")
