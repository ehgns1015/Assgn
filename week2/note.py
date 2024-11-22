# print(4 ** 0)
# sports=["tennis","football","soccer"] #Str list
# number=[1.1,2.1,3.1,4.1,5.1]#float list
# list_variable[index]
# print(sports[2])
# list_variable.append(value)
# sports.append("pingpong")
# list_variable.insert(index, value)
# sports.insert(1,"baseball")
# list_variable.pop(_index)
# sports.pop()
# sports.reverse()
# print(sports)
# sub_sports=sports[1:3]
# print(sub_sports)
# sports_str =". ".join(sports)
# print(sports_str)
# sports_list=sports_str.split(". ")
# print(sports_list)
mixed_list=[]
mixed_list.append("car")
mixed_list.append(1)
mixed_list.insert(1,True)
mixed_list.insert(0,1.1)
# print(mixed_list)
sub_mixed_list=mixed_list[0:2]
a = sub_mixed_list.pop()

# sub_mixed_list.append(1)
# print(sub_mixed_list)
sub_mixed_list2=mixed_list[2:5]
# # sub_mixed_list2.append("car")
# sub_mixed_list2.pop(1)
# print(sub_mixed_list2)
# print(a)
i = sub_mixed_list2.pop()
# print(i)
# print(sub_mixed_list,a,sub_mixed_list2,i)
sub_mixed_list.append(i)
print(sub_mixed_list)
sub_mixed_list2.append(a)
print(sub_mixed_list2)

#pop from sub_mixed_list and add it to sub_mixed_list2 [1.1], [True, 1, "car"]
#pop 1 from sub_mixed_list2 and add it to sub_mixed_list [1.1, 1], [True, "car"]
# without using constant ofc
# V=1
# I=2
# print(V*I)
