#-*- code: utf-8 -*-
import sys

def main():
    x, y, z = input("Enter the expression: ").split(" ")
    print(f"{calculate(int(x),y,int(z)):.1f}")

def calculate(x,y,z):
    
    match y:
        case "+":
            return x + z
        case "-":
            return x - z
        case "*":
            return x * z
        case "/":
            if z == 0:
                print("Division by zero error!")
                sys.exit()
            else:
                return x / z

main()
