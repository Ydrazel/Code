# -*- code: utf-8 -*-

def main():
    col=getColumns() # Call the Columns function and assign to the variable col
    row=getRows()    # Call the Rows function and assign
    drawGrid(col,row)   # Call the Grid funciton with the assigned variables

def getColumns():
    col=int(input("Enter the number of columns: "))
    return col
    
def getRows():
    row=int(input("Enter the number of rows: "))
    return row

def drawHL(col):
    print(("+"+"-"*4)*col, end="+\n")
def drawVL(col):
    print(("|"+" "*4)*col, end="|\n")

def drawGrid(col,row):
    i=row   # Assign the row variable to i for being able to iterate
    while 0<=i<=row:    # The loop that iterates through the number of rows
        if 0<=i:    # The check for horizontal lines must be bigger or equal
            drawHL(col) # Call the Horizontal line function with col num arg.
        if 0<i: # The check for vertical lines must be bigger than zero
            drawVL(col) # Call the Vertical line function with col num arg.
        i -= 1  # Decrement i variable holding the number of rows

main()
