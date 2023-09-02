# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 11:17:39 2023

@author: Asus
"""

# Accept a list of 5 float numbers as an input from the user

empyt_list = []


# Logic: while while check the condition and then new value will be appended in empty list

while len(empyt_list) < 5:
    user_input = float(input("Enter the number:- "))
    empyt_list.append(user_input)

print(empyt_list)