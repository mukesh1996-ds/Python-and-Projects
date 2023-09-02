# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 11:12:04 2023

@author: Asus
"""

# Print all factors of a given number provided by the user.

# % is used to compare if the remainder is 0 or not if 0 then print is the condition

user_value = int(input("Enter the number:- "))

for i in range(1, user_value+1):
    if user_value % i == 0:
        print(i, sep = ",")