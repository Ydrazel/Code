#-*- code: utf-8 -*-
import inflect

def main():
    p = inflect.engine()
    name_list = p.join(get_input())
    print(f"\nAdieu, adieu, to {name_list}")

def get_input():
    name_list = []
    while True:
        try:
            name = input("Name: ")
            name_list.append(name)
        except EOFError:
            break
    return name_list

if __name__=="__main__":
    main()
