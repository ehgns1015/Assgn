try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("A value error occurred")
except ZeroDivisionError:
    print("Cannot divide by zero")