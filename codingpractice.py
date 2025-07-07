# empty_set = set()
#
# fruits = {"apple","banana","cherry"}
# fruits.add("orange")
# fruits.update(["mango","kiwi"])
# fruits.remove("banana")
# # fruits.discard("pear")
# # fruits.clear()
# # # popped_item = fruits.pop()
# # print(fruits)
# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
# union = set1 | set2
# intersection = set1 & set2
# difference = set2 - set1
# difference2 = set2 - intersection
# symmetric_diff = set1 ^ set2
# symmetric2 = union - intersection
# print(union)
# print(intersection)
# print(difference)
# print(difference2)
# print(symmetric_diff)
# print(symmetric2)
# that takes two lists of numbers from the user
# converts them to sets,
# and shows their union, intersection, and difference.
list1 = []
list2 = []
list1_len = int(input("how many numbers do you want in list1?:"))
for i in range(list1_len):
    list1.append(int(input("type your number:")))

list2_len = int(input("how many numbers do you want in list2?:"))
for j in range(list2_len):
    list2.append(int(input("type your number:")))
set1 = set(list1)
set2 = set(list2)
print("Union is",set1 | set2)
print("Intersection is",set1 & set2)
print("difference is", set1 - set2)
print("symmetrical difference is",set1^set2)