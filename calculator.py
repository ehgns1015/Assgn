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
# length=int(input("write the length: "))
#
# for i in range(length):
#    n=int(input("write the number at " + str(i)+":"))
#    list.append(n)
#    print(list)
# for i in range(length):
#    list.append(i)
# print(list)
# n = input("what is the data at: ")
# total = sum(list)
# print("The sum is",sum(list))
# print ("The average is",sum(list)/len(list))
# print("The sum is",total)
# print ("The average is",total/len(list))
# print("the max is",max(list))
# print("The min is",min(list))

# x = 1
# x + 7 =8

# 1 + 7 = 8
# Create a program that uses a list to
# store the names of the days of the week,
# # then asks the user for a number (1-7) and returns the corresponding day.
# days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
# d = int(input("Pick a number from 1-7:"))
# #  d should be at least 1 and at most 7
# if 0 < d < 8:
#    print(days[d - 1])
# d = 1
# d - 1 = 0
person = {
   "name":"Ian",
   "age":12,
   "city":"Lagrange"
}
person1 = dict(name="Ian",age=12,city="Lagrange")
print(person["name"])
print(person1.get("name"))
print(person1.get("grade"))
person["grade"]= 7
removed_value = person.pop("city")
print(removed_value)
print(person)
print(person.keys(),person.values(),person.items())
person1 = person.copy()
print(person1)
# Create a simple address book program that allows users to add,
# view, and delete contacts (name and phone number) using a dictionary
person2 = {}
name = input("enter name your name:")
age = input("enter your age:")
person2["name"]=name
person2["age"]=age
print("Current data:",person2)
delete = input("Delete 'name' or 'age':")
person2.pop(delete)
print("Updated data:", person2)