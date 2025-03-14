x = str(input())

if x == 'Треугольник':
    a = int(input())
    b = int(input())
    c = int(input())

    if  a and b and c != 0:
        p = (a + b +c)/2
        print((p*(p - a)*(p - b)*(p - c))**0.5)

    else:
        print('Ошибка!')

elif x == 'Прямоугольник':
    a = int(input())
    b = int(input())
    print(a * b)

elif x == 'Круг':
    r = int(input())
    print(round(3.14*r**2, 1))

else:
    print('Неверная фигура!')
