#-*- code: utf-8 -*-
def main():
    x = input("Express your emotions!: ")
    print(convert(x))

def convert(x):
    convertedText = x.replace(":)", "🙂").replace(":(", "🙁")
    return convertedText

main()
