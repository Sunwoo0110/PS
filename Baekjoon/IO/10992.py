num = int(input())

for i in range(1, num+1):
    print(" "*(num-i), end="")
    
    for j in range(2*i-1):
        if j == 0 or j == 2*i-2 or i == num:
            print("*", end="")
        else:
            print(" ", end="")
    
    print("")