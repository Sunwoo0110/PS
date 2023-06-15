num = int(input())

for i in range(1, num+1):
    for j in range(2*num):
        if j < i or j >= 2*num - i:
            print("*", end="")
        else:
            print(" ", end="")
    print("")
    
for i in range(num-1, 0, -1):
    for j in range(2*num):
        if j < i or j >= 2*num - i:
            print("*", end="")
        else:
            print(" ", end="")
    print("")