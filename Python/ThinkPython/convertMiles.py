# -*- code: utf-8 -*-

def main():
    convertMiles()

def convertMiles():
    kMeters = int(input("Please enter the distance in Km's: "))
    miles = kMeters / 1.61
    print (f"The distance in miles is {miles:.1f}")

main()
