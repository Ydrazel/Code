#-*- code: utf-8 -*-
import re

def main():
    month, day, year = format_date()
    print(f"{year}-{month}-{day}")

def assert_input():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    
    d_months= {}
    for index, element in enumerate(months, start=1):
        d_months[index] = element

    while True:
        try:
            date = input("date: ").title()
            month, day, year = re.split("/|, | |,", date)
            if (0 < int(year)) and (1<=int(day)<=31):
                if month.isalpha() and month in d_months.values():
                    month = [k for k, v in d_months.items() if v == month]
                    month = month[0]
                    return (month, day, year)
                elif month.isdigit() and int(month) in d_months.keys():
                    return (month, day, year)
                else:
                    None
        except (ValueError, NameError):
            pass

def format_date():
    month, day, year = assert_input()
    
    if type(month) is int:
        month = f"{month:02}"
    else:
        month = month.zfill(2)

    day = day.zfill(2)
    year = year.zfill(4)
    return (month, day, year)

if __name__ == "__main__":
    main()
