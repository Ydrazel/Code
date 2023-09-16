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

    match len(sys.argv):
        case 3:
            if (sys.argv[1] == "-f") and (sys.argv[2] in font_list):
                figlet.setFont(font=sys.argv[2])
            else:
                sys.exit("Needs '-f' and a valid Font Name as arguments.")
        case 1:
            figlet.setFont(font=choice(font_list))
        case _:
            sys.exit("Needs '-f' and a valid Font Name as arguments.")

if __name__ == "__main__":
    main()
