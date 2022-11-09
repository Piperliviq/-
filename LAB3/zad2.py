numbers = int(input("Celi chisla: "))
i = 1
sum = 0
while i <= numbers:
    num = int(input(f"Vavedete chislo {i}: "))
    i += 1
    sum += num

print(sum)