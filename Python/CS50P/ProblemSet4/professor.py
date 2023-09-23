#-*- code: utf-8 -*-
from random import sample

def main():
    level = get_level()
    score = game(level)
    print(f"score: {score}")

def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl in range(1,4):
                return lvl
            else:
                pass
        except (TypeError,ValueError):
            pass

def generate_integer(level):
    while True:
        try:
            if level == 1:
                a,b = sample(range(0,10), 2)
                return (a,b)
            elif level == 2:
                a,b = sample(range(10,100), 2)
                return (a,b)
            else:
                a,b = sample(range(100,1000), 2)
                return (a,b)
        except (ValueError, KeyError):
            pass

def game(level):
    score = 0
    while True:
        try:
            j = 0
            while j < 10:
                a, b = generate_integer(level)
                i = 0
                while i < 3:
                    if int(input(f"{a} + {b} = ")) == a + b:
                        score+=1
                        break
                    else:
                        print("EEE")
                        i+=1
                else:
                    print(f">> {a} + {b} = ", a + b)
                j+=1
            return score
        except (ValueError, TypeError):
            pass

if __name__ == "__main__":
    main()
