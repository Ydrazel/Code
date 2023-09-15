#-*- code: utf-8 -*-

def main ():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    return float(d.strip("$"))

def percent_to_float(p):
    p = float(p.strip("%"))
    return p / 100

main()
