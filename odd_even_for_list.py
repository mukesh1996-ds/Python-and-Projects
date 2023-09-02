# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 13:16:18 2023

@author: Asus
"""
# get odd from list1 and even from list2

list1 = []
list2 = []
final_list = []

for i in range(1,11):
    if i%2 != 0:
        final_list.append(i)
    
    
for j in range(11,21):
    if j%2 == 0:
        final_list.append(j)
    
print(final_list)


