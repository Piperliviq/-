def can_triangle_exist(a, b, c):
    if num_1 <= num_2 + num_3 and num_2 <= num_3 + num_2 and num_3 <= num_3 + num_1:
        return 'True'
    else:
        return 'False'

num_1 = int(input("Enter side A: "))
num_2 = int(input("Enter side B: "))
num_3 = int(input("Enter side C: "))


is_valid_triangle = can_triangle_exist(num_1, num_2, num_3)
print(is_valid_triangle)
