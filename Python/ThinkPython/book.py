#-*- code: utf-8 -*-

def main():
    copy_amount = int(input("Enter the number of copies: "))
    print(f"The total wholesale cost for {copy_amount} books is:",
        round(wholesale(copy_amount),2))

def wholesale(copy_amount):
    shipping = 3+(copy_amount-1)*0.75
    price = (24.95*40/100)*copy_amount
    total = shipping + price
    return total

main()

