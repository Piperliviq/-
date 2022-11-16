s1 = {18, 19, 20}
s2 = {11, 12, 13, 15}
final_set = []
for i in s1:
    if i in s2:
        final_set = s2 - s1
    elif s2.difference(s1):
        final_set = s1 | s2
print(final_set)