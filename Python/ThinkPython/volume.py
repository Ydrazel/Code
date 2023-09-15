#-*- code: utf-8 -*-
import math

def main ():
    rad_prompt = float(input("Enter the radius of the sphere: "))
    print("The volume of the sphere is:", round(volume(rad_prompt),2))
    
def volume(radius):
    volume = 4/3*math.pi*pow(radius,3)
    return volume

main()
