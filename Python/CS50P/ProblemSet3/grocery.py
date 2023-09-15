#-*- code: utf-8 -*-
"""
Program to create a grocery list from user input
and print it sorted alphabetically with item count.
"""
def main():
    """
    Main function takes the final grocery list and iterates through it.
    """
    grocery_list = create_list()
    for k, v in grocery_list.items():
        print(f"{v} {k}")

def assert_input():
    """
    This function is responsible of ending user input loop
    and creating a raw list of items which is to be used 
    in creating the sorted item list.
    """
    raw_list = []
    while True:
        try:
            item = input().upper()
            raw_list.append(item)
        except EOFError:
            print()
            break
    return raw_list

def create_list():
    """
    In this function the raw list from the assert_input function
    is sorted and used to create the final grocery list.
    """
    raw_list = assert_input()
    sorted_list = sorted(raw_list)
    grocery_list = {i: sorted_list.count(i) for i in sorted_list}
    return grocery_list

if __name__=="__main__":
    main()
