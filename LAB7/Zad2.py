from math import sqrt
try:
    num = int(input("Enter number: "))
    print(sqrt(num))
except ValueError:
    print("Invalid number, please try again")
finally:
    print("Good bye")