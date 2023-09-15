# -*- code: utf-8 -*-
def main():
    m = int(input("Enter the number of columns: "))
    n = m + 1
    i = int(input("Enter the number of rows: "))
#   calling the final print function with all the arguments used 
    printColumns(n,m,i)
#   printRows function called to draw the bottom line
    printRows(n,m)
#   return all the variables in the main function so that they can be used as
#   arguments in printColumns function
    return n, m, i
    
def printRows(n,m):
    print(("+"+"-"*n)*m, end="+\n")
def printCells(n,m):
    print(("|"+" "*n)*m, end="|\n")
# defining the printColumns function with the returned variables from the main
# function to pass them as arguments to the functions used
def printColumns(n,m,i):
    j = 0
    while 0<=j<i:
        printRows(n,m)
        printCells(n,m)
        j += 1

main()
