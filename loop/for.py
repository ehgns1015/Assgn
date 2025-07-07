# # word= input("pick a word:")
# # for i in range(1,5):
# #     print(i)
#  # Have students write a for loop using range() to calculate the sum of all even numbers from 1 to 100.
# # sum = 0
# # # for i in range(1,101):
# # #     if i % 2 == 0:
# # #         sum += i
# # # print(sum)
# #
# # for i in range(0,101,2):
# #     sum += i
# # print(sum)
# fruits = ['apple','banana','cherry']
# for fruit in fruits:
#     print(fruit)
# for i in range(len(fruits)):
#     print(fruits[i])
# for index,fruit in enumerate(fruits):
#     print(index,fruit)
# games = ['call of duty','banana','cherry']
# for index, game in enumerate(games):
#     print(index,game)
# Have students create a dictionary of student names and grades, then write loops to:
# 1. Print only the names
# 2. Calculate the average grade
# 3. Print each student’s name with their grade

# students = {'Ian Choi':83,'Ryan Choi':98,'mom':100}
# for name in students.keys():
#     print(name)
# sum = 0
# for grade in students.values():
#     sum += grade
# average = sum/len(students.values())
# print(average)
# for name, grade in students.items():
#     print(name,grade)
# # Have students use enumerate() to create a
# # numbered list of tasks with their
# # completion status.
# # tasks = [
# #     ("Do homework", True),
# #     ("Wash dishes", False),
# #     ("Read a book", True),
# #     ("Exercise", False)
# # ]
# # for index, (task, done) in enumerate(tasks, start=1):
# #     status = "✅ Completed" if done else "❌ Not completed"
# #     print(f"{index}. {task} - {status}")
# tasks = [
#     {"task": "Do homework", "done": True},
#     {"task": "Wash dishes", "done": False},
#     {"task": "Read a book", "done": True},
#     {"task": "Exercise", "done": False}
# ]
# for index, task_info in enumerate(tasks, start=1):
#     status = "✅ Completed" if task_info["done"] else "❌ Not completed"
#     print(f"{index}. {task_info['task']} - {status}")
# # for i,task in enumerate(tasks):
# #     if task == 'cleaning' or task == 'laundry':
# #         status = True
# #         print(type(status))
# #     else:
# #         status = False
#         print(type(status))
#     print(task, status)
# Have students combine two or more lists using zip()
# to create a roster of team members with their
# positions and jersey numbers.
# names = ['john','Ryan','Aiden']
# jerseys = [13,3,28]
# positions = ['striker','defender','goalie']
# for name,jersey,position in zip(names,jerseys,positions):
#     print(f"My name is {name}, and I play {position} and my jersey number is {jersey} ")
# squares = [ x**2 for x in range(1,6)]
# print(squares)
# nums = ["even" if x % 2 == 0 else "odd"for x in range(1,6)]
# print(nums)
# Have students convert the following for loop to a
# list comprehension
# numbers = []
# for i in range(1, 21):
#     if i % 3 == 0:
#         numbers.append(i * 2)
#         print (numbers)
# number = [for i in range(1,20)]
#         numbers.append(i*2)
# numbers = [i * 2 for i in range(1,21)if i % 3 ==0]
# print(numbers)
# range(1,10) * 2
# squares = [x**2 for x in range(1, 6)]
# print(squares.)
# numb = i* 2 for i in range(1,10):

# x = [1-20]
# exp = [x * 2 for x in range(1,21)if x % 3 != 0]
# print(exp)

# Multiplication table for numbers 1 through 5

# for i in range(1, 6):  # Outer loop for rows
#     for j in range(1, 6):  # Inner loop for columns
#         product = i * j
#         print(f"{product}", end=", ")  # Format for alignment
#     print()  # New line after each row
# Have students write a loop that prints numbers from
# 1 to 20, but: - Skips multiples of 3 -
# Stops if it encounters a number divisible by
# both 3 and 5

for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        break
    if i % 3 == 0:
        continue
    print(i)
 # Have students write a for loop with an else clause
# to check if a number is prime.
num = int(input("Enter a number: "))
if num < 2:
    print("Not a prime number.")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number.")
            break
    else:
        print("Prime number!")


# Have students create a set of numbers and use a
# for loop to calculate the sum of all values.
sets = (input("enter number with spaces:"))
s = set(sets.split())
s = {int(num) for num in s}
totals = 0
for num in s:
    totals += num
print("The sum is", totals)

for i in range(11):
    if i == 5:
        pass
    print(i)