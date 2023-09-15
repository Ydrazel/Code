#-*- code: utf-8 -*-
import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def check_alpha(plate):
    while 2 <= len(plate) <= 6:
        if plate[0:1] in string.ascii_letters:
            print("First two chars are valid")
            return True
        else:
            print("First two characters must be letters")
            return False

def check_digit(plate):
    for letter in plate:
        while letter in string.digits:
            if letter == "0":
                print("First digit can not be '0'")
                return False
                break
            elif plate[-1].isalpha():
                print("Can not use digit while last char is alphabetical")
                return False
            else:
                print("No invalid digit use")
                return True

def check_type(plate):
    invalid_char = [
            letter for letter in plate
            if letter not in
            (string.ascii_letters + string.digits)
            ]
    for letter in plate:
        if any(invalid_char):
            print("Invalid Char")
            return False
        print("No invalid char")
        return True

def is_valid(plate):
    if (check_type(plate)) and (check_alpha(plate)):
        if check_digit(plate) != False:
            print("All Checks Pass..")
            return True
        else:
            return False
    else:
        False

if __name__ == "__main__":
    main()
