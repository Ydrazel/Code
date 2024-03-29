#-*- code: utf-8 -*-

def main():

    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }
    
    print("Press 'Ctrl + d' to finish your order.")

    get_order(menu)

def get_order(menu):
    total = 0
    while True:
        try:
            item = input("item: ").title()
            if item in menu:     
                total += menu.get(item)
                print(f"Total: ${total:.2f}")
        except EOFError:
            print("\n")
            break 

if __name__=="__main__":
    main()
