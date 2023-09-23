#-*- code: utf-8 -*-
from random import randint

def main():
    game()

def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl > 0:
                return lvl
            else:
                pass
        except (ValueError,TypeError):
            pass

def game():
    lvl = get_level()
    r_num = randint(1,lvl)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                if guess > r_num:
                    print("Too large!")
                elif guess < r_num:
                    print("Too small!")
                else:
                    print("Just  right!")
                    break
            else:
                pass
        except (ValueError,TypeError):
            pass

if __name__=="__main__":
    main()
