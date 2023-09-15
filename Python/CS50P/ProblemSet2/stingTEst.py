import string

string = input("enter the string: ")

def character_validation: 
    for letter in string:
        if letter.isalnum:
            print("True")
        else:
            print("False")
