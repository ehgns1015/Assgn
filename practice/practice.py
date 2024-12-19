# ===========================
# 1. Variables Practice
# ===========================
# Problem: Assign two numbers to variables and print their sum.
num1 = 5
num2 = 10
# Write the code here:
print (num1 + num2)

# Write the code here: Print the difference between num1 and num2.
print(num1 - num2)
# Write the code here: Print the product of num1 and num2.
print(num1*num2)
# Write the code here: Print the quotient of num2 divided by num1.
print(num1/num2)
# Write the code here: Print the remainder of num2 divided by num1.
print(num1 % num2)
# ===========================
# 2. Datatypes Practice
# ===========================
# Problem: Assign various datatypes to variables and print their types.
var_int = 13
var_float = 3.14
var_str = "Hello, Ian!"
var_bool = True

# Write the code here: Print the type of each variable.
print(type(var_int))
print(type(var_float))
print(type(var_bool))
print(type(var_str))
# Write the code here: Print "Hello, Ian! Are you 13 years old?" without using constants
yrs = 13
print("Hello, Ian! Are you", yrs, "years old?")
# num_of_kill = 0
# num_of_kill = num_of_kill + 1
# print(1)
# print(num_of_kill)
# ===========================
# 3. Type Casting Practice
# ===========================
# Problem: Take two numbers as input, cast them to integers, and add them together.
num_str1 = input("Enter the first number: ")
num_str2 = input("Enter the second number: ")
# Write the code here: Cast num_str1 and num_str2 to integers and print their sum.1
print (int(num_str1) + int(num_str2))
# ===========================
# 4. Comparison Operators Practice
# ===========================
# Problem: Take two numbers as input and compare them.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# Write the code here: Compare num1 and num2 and print:
# "num1 is greater" if num1 is greater,
# "num2 is greater" if num2 is greater,
# "Both numbers are equal" if they are equal.
if num1 > num2:
    print("num1 is greater")
elif num1 <= num2:
    print("num2 is greater")
else:
    print("x is greater than 5 but y is not less than 30")
# ===========================
# 5. Logical Operators Practice
# ===========================
# Problem: Take two numbers as input and print "Both numbers are even" if both are even.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# Write the code here: Check if both num1 and num2 are even using a logical operator and print the message if both are even.
# num1 and num2 are bot even
# num1 and num2 are both odd
# num1 is odd
# num2 is odd
if num1 % 2 ==0  and num2 % 2 == 0:
    print("both are even")
elif num1 % 2 !=0 and num2 % 2 !=0:
    print("both are odd")
elif num1 % 2 != 0:
    print("num 1 is odd")
else :
    print("num2 is odd")

# ===========================
# 6. List Practice
# ===========================
# Problem: Take five numbers as input and store them in a list, then print the list.
num_list = []
# Unknown Code here, Will learn Loop
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    num_list.append(num)

# Write the code here: Print all numbers stored in the list.
print(num_list)
# ===========================
# 7. Conditionals Practice
# ===========================
# Problem: Check if a given number is odd or even.
num = int(input("Enter a number: "))
# # Write the code here: Print "Odd" if the number is odd, and "Even" if the number is even.
if num % 2==0:
    (print("x is a even number"))
else:
    print("x is a odd number")
