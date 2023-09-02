# Write a program to find the euclidean distance between two coordinates.

import math # By default install while installing python else use pip install math

x_val1 = float(input("Enter the number:- "))
x_val2 = float(input("Enter the number:- "))
y_val1 = float(input("Enter the number:- "))
y_val2 = float(input("Enter the number:- "))


X = [x_val1,y_val1]
Y = [x_val2, y_val2]


equlidian_distance = math.dist(X,Y)

print(f"Equlidean distance between {X} and {Y} is {equlidian_distance}")