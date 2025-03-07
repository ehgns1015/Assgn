num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))
op=input("what to do?")
if op == "add":
    print (num1 + num2)
elif op == "subtract":
    print(num1 - num2)
elif op == "divide":
    print (num1 / num2)
elif op == "multiply":
    print (num1 * num2)
else:
    print ("error")