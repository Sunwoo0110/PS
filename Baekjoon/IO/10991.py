num = int(input())

for i in range(1, num+1):
    print(" "*(num-i), end="")
    
    for j in range(2*i-1):
        if j%2 == 0:
            print("*", end="")
        else:
            print(" ", end="")
    
    print("")