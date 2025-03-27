# num1 = int(input("enter the first number"))
# num2 = int(input("enter the second number"))
# op=input("what to do?")
# if op == "add":
#     print (num1 + num2)
# elif op == "subtract":
#     print(num1 - num2)
# elif op == "divide":
#     print (num1 / num2)
# elif op == "multiply":
#     print (num1 * num2)
# else:
#     print ("error")
#
#
# school="Long cane"
# grade="7"
#
# #Hello I am a {7}th grade student of {Long Cane} middle school
# print(f"Hello, I am a {grade}th grade student of {school} middle school")


# Hello I am {name}.I am {age} year old. My favorite color is {favorite_color}
# name = input("enter your name:")
# age = int(input("enter your age:"))
# favorite_color = input("enter your favorite color:")
# print(f"Hello I am {name}.I am {age} year old. My favorite color is {favorite_color}")

# message = "Hello I am Ian"
# messages = message.replace("Ian","Hun")
# print(messages)
# message = "Hello I am Ian"
# li = message.split(" ")
# new_message= "".join(li)
# print (new_message)
# Create a program that takes a sentence from the user
# counts how many words it contains
# and prints each word in reverse order.
# sentence = input("write your sentence: ")
# list = sentence.split(" ")
# print(list)
# print(sentence.count(" ")+1)
# for i in range(len(list)):
   # print(list[(i + 1)*-1])

# print(len(list))
# loop = n rule: loop 1 2 3 ... n - 1,  n
list=[]
# Create a program that asks the user for a list of numbers, then calculates and displays the sum, average, maximum, and minimum values.
# First ask length,
# Second input data
# Last Sum,Average,Max,Min
length=int(input("write the length: "))

for i in range(length):
   list.append(i)
print(list)
n = input("what is the data at: ")
sum = sum(list)
print("The sum is",sum)
count = len(list)
average = sum/count
print ("The average is",average)
max = max(list)
print("the max is",max)
min = min(list)
print("The min is",min)