# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 12:40:35 2023

@author: Asus
"""

# Write a program to find the simple interest when the value of principle,rate of interest and timeperiod is given.


principal_amount = int(input("Enter the value for prinicial amonut:- "))
rate_of_interest = int(input("Enter the value for rate of interest:- "))
time_period = int(input("Enter the value of given time period:- "))


# Formula to calculate simple interest 

def SimpleInterest():
    """
    This function will calculate the simple interest 
    """
    return principal_amount * rate_of_interest * time_period / 100


# Calling a function 

simple_interest = SimpleInterest()
print(simple_interest)


total_due = principal_amount + simple_interest

print(f"total amonut to be paid by the user is {total_due}")

 
