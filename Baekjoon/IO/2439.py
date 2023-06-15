num = int(input())

for i in range(num-1, -1, -1):
    for j in range(num):
        if j >= i:
            print("*", end="")
        else:
            print(" ", end="")
    print("")