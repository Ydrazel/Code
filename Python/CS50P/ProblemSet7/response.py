#-*- code: utf-8 -*-
from validator_collection import validators, errors
import sys

def main():
    print(validate(input("What's your email address?\n >>> ")))
    
def validate(s):
    while True:
        try:
            if validators.email(s):
                return f'\033[92m"Valid"\033[0m'
        except errors.EmptyValueError:
            sys.exit("No mail address given for validation!")
        except (ValueError, errors.InvalidEmailError):
            sys.exit("\033[93mInvalid Email Address\033[0m")
    
if __name__ == "__main__":
    main()
