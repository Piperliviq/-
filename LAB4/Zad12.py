import random

list_Size = random.randint(2, 50)
List_1 = []

List_1 = random.sample(range(0, 50), list_Size)
List_2 = []

for i in range(list_Size):
    if (i % 2) == 0:
        List_2.append(List_1[i])
    else:
        List_2.append((List_1[i] + List_1[i-1]))
        List_2.append(List_1[i])

print("List size:", list_Size)
print("Random list:", List_1)
print("Final list:", List_2)