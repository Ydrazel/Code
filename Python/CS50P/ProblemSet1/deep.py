#-*- code: utf-8 -*-

def checker():
    question = input("What's the answer to The Great Question of Life, the Universe, and Everything: ")
    if question == "42":
        print("Yes")
    elif question.lower() == "forty-two":
        print("Yes")
    elif question.lower() == "forty two":
        print("Yes")
    else:
        print("No")

checker()
