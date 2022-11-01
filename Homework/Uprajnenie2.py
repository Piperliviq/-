import string

symbols = string.digits + string.ascii_uppercase
number = 27102022
binary_num = ""
hex_num = ""

while number != 0:
    binary_num += str(number % 2)
    number //= 2

number = 27102022
while number != 0:
    hex_num += symbols[number % 16]
    number //= 16

print(binary_num[::-1])
print(hex_num[::-1])
