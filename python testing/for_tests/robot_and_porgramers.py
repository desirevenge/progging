num_1 = [0, 5, 6, 7, 8, 9]
num_2 = [2, 3, 4]
num_3 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

x = int(input())

if (x in num_3) or (x in num_1) or ((x > 20) and (x % 10 in num_1)) or (x % 100 in num_3):
    print(x, 'программистов')

elif (x == 1) or (x > 20) and (x % 10) == 1:
    print(x, 'программист')

elif (x in num_2) or ((x > 20) and ((x % 10) in num_2)):
    print(x, 'программиста')

else:
    print('Неверное число!')
