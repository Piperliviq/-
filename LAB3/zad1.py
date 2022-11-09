num_count = int(input('Enter number of numbers: '))
max_num = 0
i = 1
while i <= num_count:
    num = int(input(f'Enter a number {i}: '))
    if num > max_num:
        max_num = num

    i += 1
print(f"The biggest number is {max_num}")