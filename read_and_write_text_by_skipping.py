# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 11:23:27 2023

@author: Asus
"""

# Write all content of a given file into a new file by skipping line number 5

# Reading the text file 

with open ("text.txt" , "r") as text_reader:
    lines = text_reader.readlines() # inbuit fuction to readlines using this method
    print(lines)


# Opening the new text file and try to save this data into that 

with open ("new_text.txt", "w") as text_writer:
    count = 0
    for line in lines:
        if count == 4:
            count += 1
            continue
        else:
            text_writer.write(line)
            count+=1
    
    