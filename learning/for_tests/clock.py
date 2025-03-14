a = int(input())
b = int(input())
c = int(input())

if a % 60 == 0:
    x = a + ( b*60 + c )
    b = x // 60

    print(b)
    print(c)
else:
    x = a + b*60 + c
    b = x // 60
    c = 60 - ( (b+1)*60 - x)
    print(b)
    print(c)
