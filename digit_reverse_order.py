# Write a Program to extract each digit from an integer in the reverse order.

digits = input("Enter the numbers of your choise:- ")

# converting it into a list 

reverse_numbers = digits[::-1]
print(f"Reverse of the input number by the user is {reverse_numbers}")
print(f"The dtype of list1 is {type(reverse_numbers)}")


