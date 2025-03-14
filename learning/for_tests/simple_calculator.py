a = float(input())
b = float(input())
c = str(input())

if b == 0 and (c == 'mod' or c == '/' or c == 'div'):
    print('Деление на 0!')

elif c == 'mod':
    x = a % b
    print(x)

elif c == 'pow':
    x = a ** b
    print(x)

elif c == 'div':
    x = a // b
    print(x)

elif c == '+':
    x = a + b
    print(x)

elif c == '-':
    x = a - b
    print(x)

elif c == '*':
    x = a * b
    print(x)

elif c == '/':
    x = a / b
    print(x)

else:
    print('Unknown operator')
