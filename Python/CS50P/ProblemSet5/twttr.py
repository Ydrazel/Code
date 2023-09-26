#-*- code: utf-8 -*-

def main():
    string = input("Input: ")
    print(f"Output: {shorten(string)}")

def shorten(string):
    vowels = ["A", "a", "E", "e", "I", "i",
              "O", "o", "Ö", "ö", "U", "u",
              "Ü", "ü"]
    for letter in string:
        if letter in vowels:
            string = string.replace(letter, "")
    return string

if __name__ == "__main__":
    main()
