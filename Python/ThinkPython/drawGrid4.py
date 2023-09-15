#-*- code: utf-8 -*-

def main():
    col, row = getScale()
    drawGrid(col,row)

def getScale():
    col = int(input("Enter the number of Columns: "))
    row = int(input("Enter the number of Rows: "))
    return col, row

def drawGrid(col,row):
    for i in range (0,(row+1)):
        if i <= row:
            print(("+"+"-"*4)*col, end="+\n")
        if i < row:
            print(("|"+" "*4)*col, end="|\n")

main()
