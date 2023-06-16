num = int(input())
DP = {1:0}

# Topdown
def findMinTopDown(n):
    if n in DP.keys():
        return DP[n]
    
    if n%3 == 0 and n%2 == 0:
        DP[n] = min(findMinTopDown(n//3)+1, findMinTopDown(n//2)+1)
        
    if n%3 == 0 and n%2 != 0:
        DP[n] = min(findMinTopDown(n//3)+1, findMinTopDown(n-1)+1)
    
    if n%3 != 0 and n%2 == 0:
        DP[n] = min(findMinTopDown(n//2)+1, findMinTopDown(n-1)+1)
    
    if n%3 != 0 and n%2 != 0:
        DP[n] = findMinTopDown(n-1)+1
    
    return DP[n]
        
# print(findMinTopDown(num))

DP2 = [0]*(num + 1)

# BottomUp
def findMinBottomUp(n):
    for i in range(2, n+1):
        DP2[i] = DP2[i-1]+1
        if i%2 == 0: 
            DP2[i] = min(DP2[i], DP2[i//2]+1)
        if i%3 == 0:
            DP2[i]= min(DP2[i] ,DP2[i//3]+1)
    
    return DP2[n]

        
print(findMinBottomUp(num))