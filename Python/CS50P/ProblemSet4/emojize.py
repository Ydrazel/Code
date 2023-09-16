#-*- code: utf-8 -*-
import emoji

def main():
    input_string = input("input: ")
    print(f"Output: {emoji.emojize(input_string, language='alias')}")

if __name__ == "__main__":
    main()
