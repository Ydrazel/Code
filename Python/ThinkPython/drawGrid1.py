# -*- code: utf-8 -*-

def main():
    m = int(input("Enter the number of Columns: "))
    n = int(input("Enter the number of Rows: "))
    drawGrid(m,n)
    drawHL(m)
    return m, n

def drawHL(m):
    print(("+"+"-"*4)*m, end="+\n")

def drawVL(m):
    print(("|"+" "*4)*m, end="|\n")

def drawGrid(m,n):
    i = 0
    while 0 <= i < n:
        drawHL(m)
        drawVL(m)
        i += 1

main()
