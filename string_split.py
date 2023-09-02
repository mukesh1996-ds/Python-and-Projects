# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 12:24:00 2023

@author: Asus
"""

# Accept any three string from one input() call


user_input = input("Enter your name and address:- ")

split_data = user_input.split() # THis will split the user input based on space 
print(f"first word present is {split_data[0]}") # this is called indexing 
print(f"second word present is {split_data[1]}")
print(f"third word present is {split_data[2]}")
 
