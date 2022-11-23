def Pal(x):
    return x == x[::-1]

print("Enter number or word ")
x = input()

word = Pal(x)

if word:
    print("1")
else:
    print("0")
