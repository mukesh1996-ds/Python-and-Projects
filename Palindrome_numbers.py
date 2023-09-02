# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 13:12:17 2023

@author: Asus
"""

# Check Palindrome Number Write a program to check if the given number is a palindromenumber.

# A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers


user_number = int(input("Enter the number:- "))

reverse_number = str(user_number)[::-1]

print(reverse_number)

if user_number == int(reverse_number):
    print("The number is Palindrome")
else:
    print("Non-Palindrome")

    
