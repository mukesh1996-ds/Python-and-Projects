import pandas as pd

# The input text containing the syllabus
input_text = """
Beginner Level:
Introduction to Python
Python history and features
Installing Python and setting up the development environment
Python Basics
Python syntax and basic data types (e.g., numbers, strings, lists, tuples, dictionaries)
Variables, assignments, and basic operations
Input and output (I/O) operations
Control Flow
Conditional statements (if, else, elif)
Loops (while, for)
Break, continue, and pass statements
Functions
Defining functions
Parameters and return values
Lambda functions and built-in functions
Data Structures
Lists, tuples, dictionaries, and sets
Slicing and indexing
List comprehensions
File Handling
Reading and writing files
Working with CSV and JSON data
Exception Handling
Handling errors and exceptions using try-except blocks
Custom exceptions
Object-Oriented Programming (OOP) Basics
Classes and objects
Methods and attributes
Inheritance and polymorphism
Intermediate Level:
Modules and Packages
Creating and using modules
Organizing code with packages
Advanced Data Types
Collections module (Counter, defaultdict, deque, etc.)
Namedtuples and data classes
Working with Files and Directories
os and shutil modules
File manipulation, directory traversal
Regular Expressions
Pattern matching and text processing with the re module
Functional Programming
map, filter, reduce
Decorators and closures
Advanced OOP Concepts
Class methods and static methods
Magic methods
Composition and aggregation
Advanced Level:
Advanced Python Libraries
NumPy for numerical computing
Pandas for data manipulation and analysis
Matplotlib and Seaborn for data visualization
Asynchronous Programming
Understanding asyncio and async/await syntax
Web Development with Python
Introduction to Flask or Django framework
Handling HTTP requests and responses
Database Connectivity
Working with SQL databases using SQLite or SQLAlchemy
NoSQL databases (e.g., MongoDB)
Testing and Debugging
Unit testing with unittest or pytest
Debugging techniques and tools
Concurrent Programming
Threading and multiprocessing
Synchronization and communication between threads/processes
Python Best Practices and Design Patterns
Code organization and style
Common design patterns
Data Science and Machine Learning (Optional)
Exploring data with Python
Basic machine learning algorithms with scikit-learn
"""

# Split the input text into lines
lines = input_text.strip().split('\n')

# Initialize three empty lists to store data for each level
beginner_data = []
intermediate_data = []
advanced_data = []

current_level = None

# Parse the input text and store data into respective lists
for line in lines:
    if line in ["Beginner Level:", "Intermediate Level:", "Advanced Level:"]:
        current_level = line.replace(":", "")
    else:
        if current_level == "Beginner Level":
            beginner_data.append({"Level": current_level, "Topic": line})
        elif current_level == "Intermediate Level":
            intermediate_data.append({"Level": current_level, "Topic": line})
        elif current_level == "Advanced Level":
            advanced_data.append({"Level": current_level, "Topic": line})

# Create DataFrames from the data for each level
beginner_df = pd.DataFrame(beginner_data)
intermediate_df = pd.DataFrame(intermediate_data)
advanced_df = pd.DataFrame(advanced_data)

# Save DataFrames to Excel format
beginner_file = "beginner_syllabus.xlsx"
intermediate_file = "intermediate_syllabus.xlsx"
advanced_file = "advanced_syllabus.xlsx"

beginner_df.to_excel(beginner_file, index=False)
intermediate_df.to_excel(intermediate_file, index=False)
advanced_df.to_excel(advanced_file, index=False)

# Concatenate DataFrames into a single DataFrame
merged_df = pd.concat([beginner_df, intermediate_df, advanced_df], ignore_index=True)

# Save the merged DataFrame to Excel format
output_file = "python_syllabus.xlsx"
merged_df.to_excel(output_file, index=False)

print(f"Data saved to '{output_file}' successfully.")