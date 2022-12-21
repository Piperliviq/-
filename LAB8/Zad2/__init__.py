from sum import summ
from div import division
from multi import multiplication
from sub import substract
class WrongOperation(Exception):
    pass
try:
    operation = (input("Enter an operation: +, -, *, /  "))

    a = int(input('Enter number A: '))
    b = int(input('Enter number B: '))

    if b == 0 and operation == "/":
        raise ZeroDivisionError
    if operation == "+":
        summ(a, b)

    elif operation == "-":
        substract(a, b)

    elif operation == "*":
        multiplication(a, b)

    elif operation == "/":
        division(a, b)

    else:
        raise WrongOperation

except ZeroDivisionError:
    print("Numbers can't divide by 0!")

except WrongOperation:
    print("Wrong operation, please try again!")








