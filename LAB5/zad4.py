number = int(input("Enter a number: "))
def num_list(list,n):
    for i in list:
        if type(i)==int:
            if i>n:
                list[list.index(i)]=0
    return list

print(num_list([12,54,23,5,76,7,"a","y"], number))