#-*- code: utf-8 -*-
import turtle
import math

def main():
    length = int(input("Enter the length of sides: "))
    n = int(input("Enter the number of sides: "))
    r = int(input("Enter the radius for the circle: "))
    bob = turtle.Turtle()
    square(bob, length)
    polygon(bob,length,n)
    circle(bob,r)

def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t,r):
    circumference = 2 * math.pi * r
    n = 90
    length = circumference / n
    polygon(t, length, n)

main()
