num = int(input())

for i in range(1, 2*num, 2):
    for j in range(2*num-1):
        if(j < (2*num-1 - i)/2):
            print(" ", end="")
        elif (j >= (2*num-1 - i)/2+i):
            break
        else:
            print("*", end="")
    print("")