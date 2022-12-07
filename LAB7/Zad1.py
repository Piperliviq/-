try:
    f = open("Zdr.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found")
else:
    f.close()