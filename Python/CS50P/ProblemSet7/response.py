#-*- code: utf-8 -*-
from validator_collection import validators, errors
import sys

def main():
    print(validate(input("What's your email address?\n >>> ")))
    
def validate(s):
    while True:
        try:
            if validators.email(s):
                return "Valid"
        except errors.EmptyValueError:
            sys.exit("No mail address given for validation!")
        except (ValueError, errors.InvalidEmailError):
            sys.exit("Invalid Email Address")
    
if __name__ == "__main__":
    main()