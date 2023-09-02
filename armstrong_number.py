# Write a program that will check whether the number is armstrong number or not.

"""
An Armstrong number is one whose sum of digits raised to the power three equals the 
number itself. 371, for example, is an Armstrong number because 3**3 + 7**3 + 1**3 = 371.
"""

user_number = int(input("Enter the number:- "))

last_number = user_number%10
print(last_number) #3
get_last_second_number = user_number//10
print(get_last_second_number) #12
second_number = get_last_second_number%10
print(second_number) #2
first_number = get_last_second_number//10
print(first_number)

armstrong_number = (first_number**3 + second_number**3 + last_number**3)
print(armstrong_number)

# Check if the number is not an armstrong number 

if armstrong_number == user_number:
    print("Its an armstrong number")
else:
    print("Not an armstrong number")



