# Write a program that will take user input of (4 digits number) and check whether the number is narcissist number or not.

user_input=int(input("Enter the number:- "))

print(user_input)

# user input = 1234
last_number = user_input%10 #--> 4
print(last_number)
remaining_number = user_input//10 #-->123
last_third_number = remaining_number%10 #--> 3
print(last_third_number)
remaining_two_number = remaining_number//10 #-->12
last_second_number = remaining_two_number%10 #-->2
print(last_second_number)
first_number = remaining_two_number//10 #-->1
print(first_number)


narcissist_number = (first_number**4 + last_second_number**4 + last_third_number**4 + last_number**4)
print(narcissist_number)

if narcissist_number == user_input:
    print("its a narcissist number")
else:
    print("not a narcissist number")




