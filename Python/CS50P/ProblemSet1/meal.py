#-*- code: utf-8 -*-
def main():
    time = input("Enter the time of the day: ")

    if 7.00 <= float(convert(time)) <= 8.00:
        print("breakfast time")
    elif 12.00 <= float(convert(time)) <= 13.00:
        print("lunch time")
    elif 18.00 <= float(convert(time)) <= 19.00:
        print("dinner time")
    else:
        print("keep working!")

def convert(time):
    h, m = time.rsplit(":")
    minFloat = int(m) * 1.666
    if minFloat == 100.0:
        h += 1
    return  f"{h}.{round(minFloat)}"

main()
