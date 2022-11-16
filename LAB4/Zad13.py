from itertools import count

text = input("Text:")
dict_1 = {}

for i in text:
    if i not in dict_1.keys():
        dict_1[i] = text.count(i)

print(dict_1, end="")