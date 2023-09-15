#-*- code: utf-8 -*-

def main():
    greet = input("Greet the 'cunning' guy!: ").lower()
    print(Check(greet))

def Check(greet):
#    Letters = []
#    
#    for letter in greet:
#        Letters.append(letter)
    if greet.startswith("hello"):
        return ("$0")
    elif greet.startswith("h"):
        return ("$20")
    else:
        return ("$100")

main()
