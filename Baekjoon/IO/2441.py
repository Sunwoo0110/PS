num = int(input())

for i in range(num, 0, -1):
    for j in range(num):
        if j < num - i:
            print(" ", end="")
        else:
            print("*", end="")
    print("")