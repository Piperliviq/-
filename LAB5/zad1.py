def triangle(a, b):
    return a*b/2

def square(a):
    return a**2

def rectangle(a, b):
    return a*b


print("Enter an operator: tr sq rec ")

op_type = input()
a,b = eval(input("Enter two numbers: "))

if op_type == "tr":
    print(triangle(a,b))
elif op_type == "sq":
    print(square(a))
elif op_type == "rec":
    print(rectangle(a,b))
