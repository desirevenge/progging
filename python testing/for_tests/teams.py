a = int(input())
b = int(input())
d = max(a, b)

while d % b:
    d += a
print(d)
