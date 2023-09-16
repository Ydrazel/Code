# -*- code: utf-8 -*-

def main():
#    getScale()
    x = int(input("Enter the number of columns: "))
    y = int(input("Enter the number of rows: "))
    drawGrid(x,y)
    return x,y

#def getScale():
#    x = int(input("Enter the number of columns: "))
#    y = int(input("Enter the number of rows: "))
#    return x,y

def drawHL(x):
    print(("+"+"-"*4)*x, end="+\n")
def drawVL(x):
    print(("|"+" "*4)*x, end="|\n")

def drawGrid(x,y):
    i = y
    j = 0
    while 0<= i <= y:
        if 0 <= i:
            drawHL(x)
#            j+=1
        if 0 < i:
            drawVL(x)
#            j+=1
        i-=1

main()
