a = int(input("num: "))
for i in range(a):
    for j in range(a):
        if ((i == j or j == a - i - 1) and j < a // 2 or j == 0 or i == a // 2):
            print("*",end="")
        else:
            print(" ",end="")
    print()