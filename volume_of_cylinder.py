# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 12:50:36 2023

@author: Asus
"""

# Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of1litre milk is 40Rs.

# Formula = PI.R^2>H

import math 

r = float(input("Enter the number:- "))
h = float(input("Enter the number:- "))

if type(r) == float():
    pass
else:
    r = float(r)


# Volume of cylinder 
volume_of_cylinder = (math.pi * r**2 * h)
print(f"volume of cylinder is {volume_of_cylinder}")

milk_quantity = volume_of_cylinder/1000
print(f"{milk_quantity} can be loaded into the tanker")

cost_of_milk = milk_quantity*40
print(f"cost of milk is {cost_of_milk}")