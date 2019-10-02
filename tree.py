def tree(n):
    for i in range(0, int(n)):
        print((n-i) * " ", " *" * i)
    if n % 2 == 0:
        for j in range(0, int(n/2 - 1)):
            print(" " * 2, int(n - 2) * " *", " ")
    else:
        for k in range(0, int(n/2 - 1)):
            print(" " * 2, int(n - 2) * " *", " ")
print(tree(6))