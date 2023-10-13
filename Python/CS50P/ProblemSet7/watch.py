#-*- code: utf-8 -*-
import sys
import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    while True:
        try:
            m = re.search(r'^.+embed/(.*?)".+$', s)
            return f"https://youtu.be/{m.group(1)}"
        except AttributeError:
            sys.exit("None")

if __name__ == "__main__":
    main()
