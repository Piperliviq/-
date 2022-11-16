number = int(input("Enter number:"))
list_1 = []
dict_1 = {}

for i in range(1, number + 1):
    list_1.append(i)

for i in range(0, len(list_1)):
    dict_1[list_1[i]] = list_1[len(list_1) - 1 - i]

print(list_1)
print(dict_1)