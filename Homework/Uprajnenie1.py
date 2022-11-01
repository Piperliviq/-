num = int(input("Enter your number:"))
bit = int(input("Enter your bit:"))

if num & (1 << bit) > 0:
    print("False")
else:
    print("True")