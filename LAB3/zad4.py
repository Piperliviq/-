num = int(input('Vavedete chislo: '))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print('Chisloto ne e prosto')
            break
    else:
        print('Chisloto e prosto')
else:
    print('Chisloto ne e prosto')