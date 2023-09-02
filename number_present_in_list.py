# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 13:06:14 2023

@author: Asus
"""

# Write a python program to search a given number from a list


my_list = []
for i in range(1,11):
    my_list.append(i)
print(my_list)


given_number_by_user = int(input("Enter the number:- "))

if given_number_by_user in my_list:
    print(f"the {given_number_by_user} is persent inside the list")
else:
    print(f"{given_number_by_user} number is not present inside the list")
    
    
    
    


