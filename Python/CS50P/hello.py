# # Ask user for their name
# name = input("What's your name? ").strip().title()
# 
# # Remove whitespace from str and capitalize name entry
# # name = name.strip().title() carried to same line with the name variable
# # assignment
# 
# # Split user's name into first name and last name
# 
# first, last = name.split(" ")
# 
# # say hello to user
# print(f"hello, {first} {last}!")
#
# Commented out for defining a hello function

def main():
    name = input("What's your name? ")
    print(hello(name))

def hello(to="world!"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()
