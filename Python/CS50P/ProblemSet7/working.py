#-*- code: utf-8 -*-
import sys
import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    m = re.search(r'(:+?)', s)
    if m != None:
        pattern = re.search(r'^(\d+?):+(\d+?)\s+(.*?)\s+to\s+(\d+?):+(\d+?)\s+(.*?)$', s)
        return pattern.groups()
    else:
        pattern = re.search(r'^(\d+?)\s+(.*?)\s+to\s+(\d+?)\s+(.*?)$', s)
        return pattern.groups()

if __name__ == "__main__":
    main()
