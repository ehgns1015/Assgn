# 1. Separate Odd and Even Numbers from a List
# Write a program that separates the odd and even numbers in a list into two different lists.
numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = []
even_numbers = []

# Continue the same way for the rest of the list items
# let x is any number
# x % 2 = 0, that means even
# x % 2 = 1, that means odd
if numbers[0] % 2 == 0:
    even_numbers.append(numbers[0])
else:
    odd_numbers.append(numbers[0])
if numbers[1] % 2 == 0:
    even_numbers.append(numbers[1])
else:
    odd_numbers.append(numbers[1])
if numbers[2] % 2 == 0:
    even_numbers.append(numbers[2])
else:
    odd_numbers.append(numbers[2])
if numbers[3] % 2 == 0:
    even_numbers.append(numbers[3])
else:
    odd_numbers.append(numbers[3])
if numbers[4] % 2 == 0:
    even_numbers.append(numbers[4])
else:
    odd_numbers.append(numbers[4])
if numbers[5] % 2 == 0:
    even_numbers.append(numbers[5])
else:
    odd_numbers.append(numbers[5])
print("Odd numbers:", odd_numbers)
# [1, 3, 5]
print("Even numbers:", even_numbers)
# [2, 4, 6]

# 2. Find the Maximum and Minimum Values in a List
# Write a program to find the maximum and minimum values in a list.
numbers = [10, 20, 30, 40, 50]

max_num = numbers[0]
min_num = numbers[0]

# Compare the rest of the numbers similarly
if max_num < numbers[1]:
    max_num = numbers[1]
if min_num > numbers[1]:
    min_num = numbers[1]
if max_num < numbers[2]:
    max_num = numbers[2]
if min_num > numbers[2]:
    min_num = numbers[2]
if max_num < numbers[3]:
    max_num = numbers[3]
if min_num > numbers[3]:
    min_num = numbers[3]
if max_num < numbers[4]:
    max_num = numbers[4]
if min_num > numbers[4]:
    min_num = numbers[4]

print("Maximum value:", max_num)
# 50
print("Minimum value:", min_num)
# 10

# 3. Find a Specific Value in a List
# Write a program to find a specific value in a list and print its index. If not found, print "Value not found".
numbers = [10, 20, 30, 40, 50]
value = 30
if value == numbers[0]:
    print(0)
elif value == numbers[1]:
    print(1)
elif value == numbers[2]:
    print(2)
elif value == numbers[3]:
    print(3)
elif value == numbers[4]:
    print(4)
else:
    print("Value not found")


# 4. Calculate the Sum and Average of a List
# Write a program to calculate the sum and average of the values in a list.
# edit total and average
numbers = [10, 20, 30, 40, 50]
total = numbers[0]+numbers[1]+numbers[2]+numbers[3]+numbers[4]
average = total / len(numbers)
print(len("I am Groot"))
print("Sum:", total)
print("Average:", average)


# 5. Remove Duplicate Values from a List
# Write a program to remove duplicate values from a list.
numbers = [10, 20, 20, 30, 30, 40]
unique_numbers = []
if numbers[0] != numbers[1]:
    unique_numbers.append(numbers[0])
if numbers[1] != numbers[2]:
    unique_numbers.append(numbers[1])
if numbers[2] != numbers[3]:
    unique_numbers.append(numbers[2])
if numbers[3] != numbers[4]:
    unique_numbers.append(numbers[3])
if numbers[4] != numbers[5]:
    unique_numbers.append(numbers[4])
unique_numbers.append(numbers[5])

print("List without duplicates:", unique_numbers)


# 6. Find the Most Frequent Value in a List
# Write a program to find the most frequent value and its count in a list.
numbers = [10, 20, 20, 30, 30, 30, 40]

count_10 = 0
count_20 = 0
count_30 = 0
count_40 = 0

# Compare other numbers similarly

# print("Most frequent value and count:")
# Uncomment below and edit code where (edit here) is
# if (edit here):
#     print("30 appears", count_30, "times")
# elif (edit here):
#     print("20 appears", count_20, "times")
# elif (edit here):
#     print("10 appears", count_10, "times")
# else:
#     print("40 appears", count_40, "times")


# 7. Merge Two Lists
# Write a program to merge two lists into one.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# edit combined_list
combined_list = []
# print("Combined list:", combined_list)

# 8. Check if a List is in Ascending or Descending Order
# Write a program to check if a list is in ascending or descending order.
numbers = [10, 20, 30, 40, 50]

# 9. Sum of All Values in a List
# Write a program to find the sum of all values in a list.
# edit total
numbers = [1, 2, 3, 4, 5]
total = 0
# print("Sum of all values:", total)