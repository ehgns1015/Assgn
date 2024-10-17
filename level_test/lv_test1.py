# number takes between 1 and 9 as integer
number = int(input("1부터 9까지의 숫자를 입력하세요: "))

# Check number is between 1 and 9
# if so print out the times table using format
# ex)
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# if not, print out "Enter number between 1-9""
if 1 <= number <= 9:
    print(f"{number}의 구구단:")
    # 1부터 9까지의 곱셈 결과를 출력
    for i in range(1, 10):
        result = number * i
        print(f"{number} x {i} = {result}")
else:
    print("Enter number between 1-9")