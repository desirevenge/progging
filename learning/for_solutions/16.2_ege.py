def F(n):
    if n > 0:
        print("*")
        F(n - 1)
        F(n // 3)

print(F(6))
