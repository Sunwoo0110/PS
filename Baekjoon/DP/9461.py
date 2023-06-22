tc_num = int(input())

for i in range(tc_num):
    num = int(input()) 
    DP = [0]*(100+1)
    DP[1] = 1
    DP[2] = 1
    DP[3] = 1
    DP[4] = 2
    DP[5] = 2
    
    for j in range(6, num+1):
        DP[j] = DP[j-1] + DP[j-5]
        
    print(DP[num])