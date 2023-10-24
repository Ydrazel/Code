#-*- code: utf-8 -*-
import sys
import inflect
from datetime import date,timedelta

def main():
    i = get_date(input("Date of Birth: "))
    print(convert(i))

def get_date(s):
    while True:
        try:
            year, month, day = [int(item) for item in s.split('-')]
            birth_date = date(year, month, day)
            today = date.today()
            delta = (today - birth_date).days
            minutes = delta * (24 * 60)
            return minutes
        except ValueError:
            sys.exit("Input should be in format YYYY-MM-DD")

def convert(m):
    p = inflect.engine()
    words = p.number_to_words(m, andword="")
    return f"{words} minutes"

if __name__ == "__main__":
    main()
