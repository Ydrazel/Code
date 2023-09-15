#-*- code: utf-8 -*-

def main():
    string = input("Input: ")
    converter(string)

def converter(string):
    vowels = ["A", "a", "E", "e", "I", "i",
              "O", "o", "Ö", "ö", "U", "u",
              "Ü", "ü"]
    string = [(f"") if letter in vowels
              else letter for letter in string]
    print("Output: ", *string, sep="")

if __name__ == "__main__":
    main()
