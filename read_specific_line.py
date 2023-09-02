# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 12:37:25 2023

@author: Asus
"""

# Read line number 4 from the following file

with open ("new_text.txt", "r") as read_text:
    lines = read_text.readlines()
    print(lines[3])