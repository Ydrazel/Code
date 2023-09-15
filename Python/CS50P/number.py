# try:
#     x = int(input("What's x? "))
# #    print(f"x is {x}")
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")

def main():
    x=get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
#            break
        except ValueError:
#            print("x is not an integer")
            pass

main()

# print(f"x is {x}") calling print after the exception VAlueError causes a name
# error. using else: is needed
