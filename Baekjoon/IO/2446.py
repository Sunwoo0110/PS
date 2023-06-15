num = int(input())

for i in range(0, num):
    for j in range(2*num-1):
        if j < i:
            print(" ", end="")
        elif j >= 2*num - 1 - i:
            break
        else:
            print("*", end="")
    print("")
    
for i in range(num-2, -1, -1):
    for j in range(2*num-1):
        if j < i:
            print(" ", end="")
        elif j >= 2*num - 1 - i:
            break
        else:
            print("*", end="")
    print("")