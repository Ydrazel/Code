#-*- code: utf-8 -*-
def main():
    converter()

def converter():
    variable = input("Enter Variable Name: ")
    variable = [
            (f"_{letter.lower()}") if letter.isupper() 
            else letter for letter in variable
            ]
    print(*variable, sep="")

if __name__ == "__main__":
    main()
