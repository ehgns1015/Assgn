# from fractions import Fraction

class Calculator:
    # Delete this line and create a Constructor
    """
    Constructor

    Parameters:
    no

    *Note
    If you don't know how to create a constructor,
    then comment line #3 and the codes below "Execute"
    """
 
    def __init__(self):
        pass

    def add(self, num1, num2):
        """
        Add two numbers.

        Parameters:
        num1 (float): The first number.
        num2 (float): The second number.

        Returns:
        float: The sum of num1 and num2.
        """
        return num1 + num2

    def subtract(self, num1, num2):
        """
        Subtract the second number from the first number.

        Parameters:
        num1 (float): The first number.
        num2 (float): The second number.

        Returns:
        float: The difference of num1 and num2.
        """

        return num1 - num2

    def multiply(self, num1, num2):
        """
        Multiply two numbers.

        Parameters:
        num1 (float): The first number.
        num2 (float): The second number.

        Returns:
        float: The product of num1 and num2.
        """
        return num1 * num2

    def divide(self, num1, num2):
        """
        Divide the first number by the second number.

        If the second number is zero, a warning message is returned.

        Parameters:
        num1 (float): The numerator.
        num2 (float): The denominator.

        Returns:
        Float or str: The result of the division as a float,
                         or a message indicating division by zero.
        """
        if num2 == 0:
            return "Nothing divided by 0"
        else:
            return num1 / num2
        
    def calculate(self, num1, num2, operation):
        """
        Perform a calculation based on the given operation.

        Parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform. Can be one of '+', '-', '*', '/'.

        Returns:
        float, Fraction, or str: The result of the calculation or a message for invalid operations.
        """
        match operation:
            case "+":
                return self.add(num1, num2)
            case "-":
                return self.subtract(num1, num2)
            case "*":
                return self.multiply(num1, num2)
            case "/":
                return self.divide(num1, num2)
            case _:
                return "Invalid operation."

# Execute
if __name__ == "__main__":
    "Assign the Calculator object to calc"
    calc = Calculator()

    #num1 takes value from the console typed input after "Input for num1: ""
    num1 = float(input("Input for num1: "))
    #num2 takes value from the console typed input after "Input for num2: ""
    num2 = float(input("Input for num2: "))
    #operation takes value from the console typed input after "Choose Operation (+, -, *, /): ""
    operation = input("Choose Operation (+, -, *, /): ")
    #assign the result of calculation"
    result = calc.calculate(num1, num2, operation)
    #print out the result after "Result:""
    print("Result:", result)