#-*- code: utf-8 -*-

def main():
    fuel()

def get_frac():
    while True:
        try:
            S = input("Enter the fraction: ").split("/")
            I = [int(i) for i in S]
            return I
        except (ValueError, ZeroDivisionError):
            pass

def fuel():
    X, Y = get_frac()
    while Y == 0 | Y < X:
        X, Y = get_frac()
    Z = X/Y

    if Z <= 1/100:
        print("E")
    elif 99/100 <= Z:
        print("F")
    else:
        percent = round(Z*100)
        print(f"{percent}%")

if __name__ == "__main__":
    main()
