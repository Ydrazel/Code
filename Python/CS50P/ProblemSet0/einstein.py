#-*- code: utf-8 -*-
def main():
    m = int(input("Enter the mass in kilograms: "))
    print(calculate(m))

def calculate(m):
    c = 3000000000
    E = m * pow(c,2)
    return E

main()
