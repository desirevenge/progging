a = int(input())
b = int(input())
c = int(input())

maxim = a
minim = b

if b > a:
    maxim = b
    minim = a

if c > maxim:
    maxim = c

if c < minim:
    minim = c

ost = a + b + c - maxim - minim

print(maxim)
print(minim)
print(ost)
