# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 13:03:43 2023

@author: Asus
"""

# Print the sum of the current number and the previous number 
# Write a program to iterate the first10 numbers and in each iteration, 
# print the sum of the current and previous number.



previous_number = 0

# for loop

for i in range(1,11):
    x = i+previous_number
    previous_number=1
    print(x, sep=" ")