# print("What is 7*5")
# print("It is", 7*5)
# print("Hi nice to meet you")
# print("Sorry")
# print("Hello")
# #The meaning is "Hi"
# print("")
# #My name
# print("I am 30 years old")
# #Mistake of age
# import requests
# #
# def get_public_ip():
#     try:
#         response = requests.get('https://api.ipify.org?format=json')
#         ip_data = response.json()
#         return ip_data['ip']
#     except requests.exceptions.RequestException as e:
#         return f"Error: {e}"
#
# if __name__ == "__main__":
#     ip = get_public_ip()
#     print(f"Your public IP address is: {ip}")
# 1-100 count odd, even, divided by 3, and one which is even and divided by 3
# odd numbers: #
# even numbers: #
# multiples of 3: #
# multiples of 3 and also even : #
# odd=0
# even=0
# mo3=0
# mo3_even=0
# for i in range(1,101):
#     # print(i)i
#     if i % 2 != 0:
#         odd=odd+1
# print("odd numbers:",odd)
# for i in range(1,101):
#     if i % 2 ==0:
#         even=even+1
# print("even numbers",even)
# for i in range(1,101):
#     if i % 3 ==0:
#         mo3 = mo3 + 1
# print("mo3 numbers",mo3)
# for i in range(1,101):
#     if i % 6 ==0:
#         mo3_even=mo3_even+1
# print("mo3_even numbers",mo3_even)

n = [10, 20, 20, 30, 30, 30, 40]

count_10 = 0
count_20 = 0
count_30 = 0
count_40 = 0
#
# print(n[0])
# print(n[1])
# print(n[2])
# print(n[3])
# print(n[4])
# print(n[5])
# # print(n[6])
for num in n:
    # print(num)
    if num==10:
        count_10 += 1
    elif num==20:
        count_20 += 1
    elif num==30:
        count_30 +=1
    elif num==40:
        count_40 += 1
print("10 appears",count_10,"time" if count_10 < 2 else "times")
print("20 appears",count_20,"time" if count_20 < 2 else "times")
print("30 appears",count_30,"time" if count_30 < 2 else "times")
print("40 appears",count_40,"time" if count_40 < 2 else "times")
