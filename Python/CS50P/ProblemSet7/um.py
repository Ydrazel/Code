#-*- code: utf-8 -*-
import sys
import re

def main ():
    print(count(input("Text: ")))

def count(s):
    m = re.findall(r'(?<!\S)um(?=\W|$)', s, re.IGNORECASE)
    return len(m)

if __name__ == "__main__":
    main()
