""" Question 2 and 3
Now try to develop a call for calculator which perform add, sub, mul and div operations

Create a parent class where it will ask the user input, Validate this and then pass to
calculator class , (Basically calculator class will inherit this parent class for getting
input numbers and to check if they are valid numbers)
"""
from decimal import Decimal
import re


class Input:

    def __init__(self):

        input1 = input("Enter the first number: ")
        pattern = re.compile(r'^[0-9+-]\.?[0-9]*$')
        match1 = pattern.match(input1)
        while match1 is None:
            input1 = input("Please Enter the valid first number: ")
            match1 = pattern.match(input1)
        self.a = Decimal(match1.group())
        input2 = input("Enter the second number: ")
        match2 = pattern.match(input2)
        while match2 is None:
            input2 = input("Please Enter the valid second number: ")
            match2 = pattern.match(input2)
        self.b = Decimal(match2.group())


class Calculator(Input):

    def __init__(self):
        super().__init__()


    def add(self):
        print("{} + {} = {}".format(self.a, self.b, self.a + self.b))
        return self.a + self.b

    def sub(self):
        print("{} - {} = {}".format(self.a, self.b, self.a - self.b))
        return self.a - self.b

    def mul(self):
        print("{} * {} = {}".format(self.a, self.b, self.a * self.b))
        return self.a * self.b

    def div(self):
        try:
            print("{} / {} = {}".format(self.a, self.b, round(self.a / self.b, 3)))
            return self.a / self.b
        except:
            print("Division by zero is not allowed")


calc = Calculator()
calc.add()
calc.sub()
calc.mul()
calc.div()



