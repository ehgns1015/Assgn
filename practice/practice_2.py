# solve with for loop
# 1. Separate Odd and Even Numbers from a List
# Write a program that separates the odd and even numbers in a list into two different lists.
numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = []
even_numbers = []

# Continue the same way for the rest of the list items
# let x is any number
# x % 2 = 0, that means even
# x % 2 = 1, that means odd
# for i in range( len(numbers)):
#     if numbers[i] % 2 ==0:
#         even_numbers.append(numbers[i])
#     elif numbers[i] % 2!=0:
#         odd_numbers.append(numbers[i])
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        even_numbers.append(numbers[i])
    else:
        odd_numbers.append(numbers[i])
    i += 1
# for n in range(len(numbers)):
#     if numbers[n] % 2 == 0:
#         even_numbers.append(numbers[n])
#     else:
#         odd_numbers.append(numbers[n])
# if numbers[0] % 2 == 0:
#     even_numbers.append(numbers[0])
# else:
#     odd_numbers.append(numbers[0])
# if numbers[1] % 2 == 0:
#     even_numbers.append(numbers[1])
# else:
#     odd_numbers.append(numbers[1])
# if numbers[2] % 2 == 0:
#     even_numbers.append(numbers[2])
# else:
#     odd_numbers.append(numbers[2])
# if numbers[3] % 2 == 0:
#     even_numbers.append(numbers[3])
# else:
#     odd_numbers.append(numbers[3])
# if numbers[4] % 2 == 0:
#     even_numbers.append(numbers[4])
# else:
#     odd_numbers.append(numbers[4])
# if numbers[5] % 2 == 0:
#     even_numbers.append(numbers[5])
# else:
#     odd_numbers.append(numbers[5])
print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)


# 2. Find the Maximum and Minimum Values in a List
# Write a program to find the maximum and minimum values in a list.
numb = [10, 20, 30, 40, 50]

max_num = numb[0]
min_num = numb[0]

# # Compare the rest of the numbers similarly
# for i in range(1,len(numb)):
#     if numb[i] > max_num:
#         max_num = numb[i]
#     if numb[i] <  min_num:
#         min_num = numb[i]
i = 1
while i < len(numb):
    if numb[i] > max_num:
        max_num = numb[i]
    if numb[i] < min_num:
        min_num = numb[i]
    i += 1

# for num in numb[1:]:
#     if num > max_num:
#         max_num = num
#     if num < min_num:
#         min_num = num
# for i in range(1, len(numb)):
#     if numb[i] > max_num:
#         max_num = numb[i]
#     if numb[i] < min_num:
#         min_num = numb[i]
# if max_num < numbers[1]:
#     max_num = numbers[1]
# if min_num > numbers[1]:
#     min_num = numbers[1]
# if max_num < numbers[2]:
#     max_num = numbers[2]
# if min_num > numbers[2]:
#     min_num = numbers[2]
# if max_num < numbers[3]:
#     max_num = numbers[3]
# if min_num > numbers[3]:
#     min_num = numbers[3]
# if max_num < numbers[4]:
#     max_num = numbers[4]
# if min_num > numbers[4]:
#     min_num = numbers[4]

print("Maximum value:", max_num)
print("Minimum value:", min_num)

# 3. Find a Specific Value in a List
# Write a program to find a specific value in a list and print its index. If not found, print "Value not found".
numbers = [10, 20, 30, 40, 50]
value = 30
# for number in range(len(numbers)):
#     if numbers[number] == value:
#         print(number)
#         break
#     if number  == len(numbers) - 1:
#         print("value not found")
number = 0
while number < len(numbers):
    if numbers[number] == value:
        print(number)
        break
    if number == len(numbers) - 1:
        print("value not found")
    number += 1
# if value in numbers:
#     print(numbers.index(value))
# else:
#     print("Value not found")
#
# # from 1-100 print out only odd number using continue
# for i in range(1,101):
#     if i % 2 == 0:
#         continue
#     print(i)
# list[start:end+1]
# range(start, end+1)
# print(numbers[1:])
# print(range(1,len(numbers)))
# for i in range(1,len(numbers)):
#     print(i)
# for i in range(len(numbers)):
#     if value == numbers[i]:
#         print("found")
#         break
#     if i == len(numbers) - 1:
#         print("value not found")
# if value in numbers:
#     # If found, print the index of the value
#     index = numbers.index(value)
#     print(f"Value {value} found at index {index}")
# else:
#     # If not found, print a message
#     print("Value not found")

# # 4. Calculate the Sum and Average of a List
# # Write a program to calculate the sum and average of the values in a list.
# # edit total and average
number = [10, 20, 30, 40, 50]
total = 0
average = 0
# Calculate the sum of the numbers
# for i in number:
#     # print("i is",i )
#     total += i
#     print("total is", total)
#     # total += number i]
#
# average= total / len(numbers)
number = [10, 20, 30, 40, 50]
total = 0
average = 0

i = 0
while i < len(number):
    total += number[i]
    print("total is", total)
    i += 1

average = total / len(number)
print("average is", average)



# for i in range(len(numbers)):
#     total += numbers[i]
#
# if len(numbers) > 0:
#     average = total / len(numbers)
# Before starting the loop you initialize both variable as 0 then after that the after that you go every single index. Then each time you go through an index you add the value to the total.
# Then lastly you divide the total by the length of the numbers then you get the average.
# Print the results
print("Total:", total)
print("Average:", average)
#
# print("Sum:", total)
# print("Average:", average)
#
#
# # 5. Remove Duplicate Values from a List
# # Write a program to remove duplicate values from a list.
# num = [10, 20, 20, 30, 30, 40]
# unique_numbers = []
# # Iterate over the original list and add items to unique_numbers if not already present
# for number in num:
#     if number not in unique_numbers:
#         unique_numbers.append(number)
# print("List without duplicates:", unique_numbers)
num = [10, 20, 20, 30, 30, 40]

unique_numbers = []
# range(start,end+1)
# range(4)=0,1,2,3
# for i in range(len(num)):
#     if num[i] not in unique_numbers:
#         unique_numbers.append(num[i])
#
#
# print("List without duplicates:", unique_numbers)
num = [10, 20, 20, 30, 30, 40]
unique_numbers = []

i = 0
while i < len(num):
    if num[i] not in unique_numbers:
        unique_numbers.append(num[i])
    i += 1

print("List without duplicates:", unique_numbers)
# It first checks if the index that refers to num at the time is in the list and if it is not it puts it into the list. So if there is a repeating it does not put it into the list.
# 6. Find the Most Frequent Value in a List
# Write a program to find the most frequent value and its count in a list.
n = [10, 20, 20, 30, 30, 30, 40]

count_10 = 0
count_20 = 0
count_30 = 0
count_40 = 0

x=[]



counts = {}
# for num in n:
#     counts[num] = counts.get(num, 0) + 1
#
# most_frequent_value = max(counts, key=counts.get)
# max_count = counts[most_frequent_value]
# n = [10, 20, 20, 30, 30, 30, 40]

counts = {}
i = 0
while i < len(n):
    num = n[i]
    counts[num] = counts.get(num, 0) + 1
    i += 1

most_frequent_value = max(counts, key=counts.get)
max_count = counts[most_frequent_value]

print("Most frequent value:", most_frequent_value)
print("Count:", max_count)

# print(f"The most frequent value is {most_frequent_value} with a count of {max_count}.")
# the counts.get(num,0) it makes the list start at zero and add 1 if the number wasnt already there to most frequent value
# the max(counts, key=counts.get finds the number with the highest count
# then they print
# # Compare other numbers similarly
# for num in n:
#     if num == 10:
#         count_10 += 1
#     elif num == 20:
#         count_20 += 1
#     elif num == 30:
#         count_30 += 1
#     elif num == 40:
#         count_40 += 1
#
# # Find the most frequent number and its count
# max_count = max(count_10, count_20, count_30, count_40)
#
# if max_count == count_10:
#     print(f"Most frequent value: 10, Count: {count_10}")
# elif max_count == count_20:
#     print(f"Most frequent value: 20, Count: {count_20}")
# elif max_count == count_30:
#     print(f"Most frequent value: 30, Count: {count_30}")
# elif max_count == count_40:
#     print(f"Most frequent value: 40, Count: {count_40}")
# print("Most frequent value and count:")
# # Uncomment below and edit code where (edit here) is
# if count_30 > count_20 and count_30 > count_10 and count_30 > count_40:
#     print("30 appears", count_30, "times")
# elif count_20 > count_10 and count_20 > count_30 and count_20 > count_40:
#     print("20 appears", count_20, "times")
# elif count_10 > count_20 and count_10 > count_30 and count_10 > count_40:
#     print("10 appears", count_10, "times")
# else:
#     print("40 appears", count_40, "times")
#
#
# # 7. Merge Two Lists
# # Write a program to merge two lists into one.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# edit combined_list
combined_list = []

# for item in list1:
#     combined_list.append(item)
# for item in list2:
#     combined_list.append(item)
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
i = 0
while i < len(list1):
    combined_list.append(list1[i])
    i += 1
j = 0
while j < len(list2):
    combined_list.append(list2[j])
    j += 1
# # Print the merged list
print("Combined list:", combined_list)
#for the first loop it looks at every single numbers in list1 and appends it to combined_list.
# for the second loop it looks at every single number in list2 and appends it to combined_lisst
# then it prints it
# # 8. Check if a List is in Ascending or Descending Order
# # Write a program to check if a list is in ascending or descending order.
numbers = [10, 20, 30, 40, 50]
ascending = True
descending = True
# #
# for i in range(len(numbers) - 1):
#     if numbers[i] > numbers[i + 1]:
#         ascending = False
#     elif numbers[i] < numbers[i + 1]:
#         descending = False
# #
# if ascending:
#     print("The list is in Ascending order")
# elif descending:
#     print("The list is in Descending order")
# else:
#     print("The list is Unordered")
i = 0
while i < len(numbers) - 1:
    if numbers[i] > numbers[i + 1]:
        ascending = False
    elif numbers[i] < numbers[i + 1]:
        descending = False
    i += 1

if ascending:
    print("The list is in Ascending order")
elif descending:
    print("The list is in Descending order")
else:
    print("The list is Unordered")

#we first see if the list is assending by checking each of the indexs. If they are bigger tahan the next number put ascending to false
# same with descending if the number is smaller than the next number, put descending at false
# then print the result.
# # 9. Sum of All Values in a List
# # Write a program to find the sum of all values in a list.
# # edit total
numbers = [1, 2, 3, 4, 5]
total = 0
# for num in numbers:
#     total += num
i = 0
while i < len(numbers):
    total += numbers[i]
    i += 1
# Print the total sum
print("The sum of all values in the list is:", total)
# the total first stays at zero
# use the for loop to iterate through each number
# Use the iterated values and add it to total
# Finally print total