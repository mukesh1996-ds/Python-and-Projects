# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 12:33:21 2023

@author: Asus
"""

# Check file is empty or not Write a program to check if the given file is empty or not

import os

size = os.stat("new_text.txt").st_size

if size == 0:
    print("The file is empty")
else:
    print("file is not epmty")
    