def sum_nums(a, b):
    return a+b

def sub_nums(a, b):
    return a-b

def dev_nums(a, b):
    return a/b

def multi_nums(a, b):
    return a*b

print("Enter an operator: + - / * ")

op_type = input()
a,b = eval(input("Enter two numbers: "))

if op_type == "+":
    print(sum_nums(a,b))
elif op_type == "-":
    print(sub_nums(a,b))
elif op_type == "/":
    print(dev_nums(a,b))
elif op_type == "*":
    print(multi_nums(a,b))
