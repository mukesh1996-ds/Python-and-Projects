"""
 Python is a popular, high-level programming language known for its simplicity and readability. 
 It was created by Guido van Rossum and first released in 1991. Here are some basic concepts and 
 features of Python:
"""

# Print Statement: In Python, you can use the print() function to display output on the screen. For example:
print("Hello World")

# Variables and Data Types: You can assign values to variables in Python. Python is dynamically typed, 
# meaning you don't need to declare the data type explicitly.

# Integer
age = 25
data_type = type(age)
print(f"user age is {age} and its dtype is {data_type}")
      

# Float
height = 5.9
print(f"height of the person is {height} and its data type is: {type(height)}")

# String
name = "John Doe"
print("{} is the name of the person and I love him really from my foot".format(name))

# Boolean
is_student = True

# Basic Arithmetic Operations: Python supports standard arithmetic operations:

a = 10
b = 5

sum_result = a + b
print(sum_result)
difference_result = a - b
print(difference_result)
product_result = a * b
print(product_result)
division_result = a / b
print(division_result)
modulus_result = a % b  # remainder of a divided by b
print(modulus_result)
# Conditional Statements: Python uses if, elif, and else for conditional branching:

age = 18

if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just reached adulthood.")
else:
    print("You are an adult.")


# Loops: Python supports for and while loops for iteration:
# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1


# Lists: Lists are a collection of items in Python and can contain different data types:

fruits = ["apple", "banana", "orange"]

print(f"{fruits} are stored in the form of {type(fruits)}")

# Functions: Functions are blocks of reusable code:

def greet(name):
    print("Hello, " + name + "!")

print(greet("Alice"))

# Modules: Modules are Python files containing functions and variables that can be imported and reused 
# in other scripts:
# In a separate file named mymodule.py
def add(a, b):
    return a + b

# In your main script
import math
result = math.sqrt(2)
print(result)

# Comments: Use # to write single-line comments and ''' ... ''' or """ ... """ for multi-line comments.

# This is a single-line comment

'''
This is a
multi-line comment
'''
"""

These are just some of the basic concepts in Python. As you progress, you'll encounter more advanced 
topics like classes, objects, file handling, and more. Python has a vast standard library and a vibrant 
community, making it suitable for various applications, from web development to data science and automation.

"""
