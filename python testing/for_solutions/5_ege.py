for n in range(1, 100):
    b=bin(n)[2:]
    if n%2==0:
        b = '10' + b
    else:
        b = '1'+b+'01'
    r = int(b,2)
    if r >= 19:
        print(n)
