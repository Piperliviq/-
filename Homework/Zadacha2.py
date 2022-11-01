from math import pi

r = float(input())
perimetar = 2 * pi * r
S = pi * r**2
perimetar = float(round(perimetar, 3))
S = float(round(S, 3))

print(perimetar)
print(S)