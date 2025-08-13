# def print_list(li,num):
#     if num < len(li):
#         print(li,[num])
#         print_list(li,num +1)
# def numplay(num):
#     # odd => 2*num+1
#     # even => int(num/2) - 1
#     if num > 0:
#         print(num)
#         if num % 2 ==1:
#             numplay(2+num)
#         else:
#             numplay(int[num/2)-1)
def sum_to_n(n):
    if n == 0:
        return n
    return n+ sum_to_n(n-1)
print(sum_to_n(5))

