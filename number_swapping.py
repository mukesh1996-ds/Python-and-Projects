# Swapping the first and second number without using 3 number 

"""
If I use input function to take the user input from Terminal I need to use convert this into int else it will
be in string format.
"""

num1 = int(input("Enter the number of your choice:-"))
num2 = int(input("ENter the number of your choice:-"))


print(f"user enter the numbers are {num1} and {num2}")

# The above method is called Type casting 

# Lets apply logic

"""
eg: num1 = 2 and num2 = 3 in first num1 = 5
                            second num2 = -1
                            num1 = 5-1 = 4

"""
num1 = num1 + num2 # output = 20
num2 = num1 - num2 # output = 9
num1 = num1 - num2 # output = 20 - 9 = 11

print(num1)
print(num2)

