#-*- code: utf-8 -*-
from pyfiglet import Figlet
from random import choice
import sys

def main():
    figlet = Figlet()
    set_font(figlet)
    s = input("Input: ")
    print(f"Output:\n{figlet.renderText(s)}")

def set_font(figlet):
    font_list = figlet.getFonts()

    while len(sys.argv) == 3:
        if (sys.argv[1] in ("-f", "--font")) and (sys.argv[2] in font_list):
            figlet.setFont(font=sys.argv[2])
            break
        else:
            sys.exit("needs -f and font name as argumnets")
    else:
        figlet.setFont(font=choice(font_list))

if __name__ == "__main__":
    main()
