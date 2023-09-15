#-*- code: utf-8 -*-
def main():
    machine()

def machine():
    amount_due = 50
    accepted_coins = [25, 10, 5]
    while amount_due <= 50:
        if amount_due > 0:
            print(f"Amount Due: {amount_due}")
            coin = int(input("Insert Coin: "))
            if coin in accepted_coins:
                amount_due -= coin
            else:
                None
        else:
            print(f"Change Owed: {-amount_due}")
            break

if __name__ == "__main__":
    main()
