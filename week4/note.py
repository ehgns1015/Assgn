# # 1. assign [Fortnite,Elden Ring,Call of Duty] to a variable called "games".
# games_str = "fortnite,elden ring,call of duty"
# games_list = games_str.split(",")
# print(games_list)
# games_list.insert(2,"LOL")
# print(games_list)

# if boolean(condition):
#   statement

# num = int(input("Please enter the number: "))
# print(num % 2 == 1)
# x = int(input("Please enter the number: "))
#
x=10
y =30
if x % 2 != 0 or x % 5 !=0:
    print("x is not good number")
elif x % 5 != 0:
    print("x is not good number")
else:
    print("x is a good number")
#
# x = 10
# y = 30

# if x > 5:
#     if y < 30:
#         print("x is greater than 5 and y is less than 30")
#     elif x > 15:
#         print("x is greater than 15 and y is greater than 30")
#     else:
#         print("x is greater than 5 but y is not less than 30")
# else:
#     print("x is not greater than 5")

x = int(input("Enter a number: "))
result = "x is even" if x % 2 ==0 else "x is odd"
print(result)
