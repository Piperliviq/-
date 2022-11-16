number = int(input("Enter number:"))
list_1 = []
result = 1

for i in range(0, number):
    if i == 0:
        list_1.append(number)
    else:
        list_1.append(list_1[i - 1] * 10 + number)

for i in range(0, number):
    result += list_1[i]
    print(end=f"{list_1[i]}")
    if i != (number - 1):
        print(end="+")
    else:
        print(end="=")

print(result)