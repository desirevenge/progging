while True:
    a = int(input())
    if a < 10 and a < 100:
        continue
    elif a > 100:
        break
    print(a)
