# Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

num = input("Enter the number:-  ")


reverse_number = num[::-1]

print(reverse_number)
# Wil write a condition to check if the number is revers of my input is true or not

if (num != reverse_number):
    print(f"Number is reverse {reverse_number}")
