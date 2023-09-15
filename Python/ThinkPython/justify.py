#-*- code: utf-8 -*-
def main():
    right_justify(input("What's your name? "))
def right_justify(name):
    print(" "*(70-len(name)) + name)
main()
