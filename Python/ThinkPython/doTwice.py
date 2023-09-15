#-*- code: utf-8 -*-
import math

def main():
    h = input("What's your name? ")
    do_quad(f,h)
def do_twice(f,h):
    f(h)
    f(h)
def do_quad(f,h):
    do_twice(f,h)
    do_twice(f,h)
def f(name):
    print("-"*math.floor((70-len(name))/2) + name + "-"*math.floor((70-len(name))/2))

main()
