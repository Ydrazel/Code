# -*- code: utf-8 -*-

def main():
    x = int(input("Enter the number of columns: "))
    y = int(input("Enter the number of rows: "))
    drawGrid(x,y)
    return x,y

def drawHL(x):
    print(("+"+"-"*4)*x, end="+\n")
def drawVL(x):
    print(("|"+" "*4)*x, end="|\n")

def drawGrid(x,y):
    i = y
    while 0<= i <= y:
        if 0 <= i:
            drawHL(x)
        if 0 < i:
            drawVL(x)
        i-=1

if __name__=="__main__":
    main()
