# -*- code: utf-8 -*-

def main():
    convert()

def convert():
    minutes = int(input("Please enter minutes: "))
    seconds = int(input("Please enter seconds: "))
    secTotal = minutes * 60 + seconds
    print (f"Total time in seconds is {secTotal}")

main()
