# Write a program to find the sum of 3 digits 

number = int(input("Enter the number:- "))

a = number%10  # last digit
print(a) # --3
b = number//10 # first 2 digit
print(b) #--12
c = b%10 # last digit store in b
print(c) #--2
d = b//10 # first digit
print(d) #--
print(a+c+d)

