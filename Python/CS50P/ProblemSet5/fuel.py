#-*- code: utf-8 -*-

def main():
    fraction = input("Enter the fraction: ")
    if convert(fraction) != None:
        print(gauge(convert(fraction)))

def convert(s):
    try:
        s = s.split("/")
        j = [int(i) for i in s]
        x, y = j
        if x <= y:
            z = x / y
            return round(z*100)
        elif y == 0:
            raise ZeroDivisionError
            pass
        else:
            raise ValueError
            pass
    except ValueError:
        raise ValueError
        pass
    except ZeroDivisionError:
        raise ZeroDivisionError
        pass

def gauge(z):

    if z <= 1:
        return "'E'"
    elif 99 <= z:
        return "'F'"
    else:
        return f"{z}%"

if __name__ == "__main__":
    main()
