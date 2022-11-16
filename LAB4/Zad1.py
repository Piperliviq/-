fib = []
number = int(input("Enter numbers:"))

for i in range(0, number + 2):
    if i == 0:
        fib.append(0)
    elif i == 1:
        fib.append(1)
    else:
        fib.append(fib[i-1] + fib[i-2])

print(fib)