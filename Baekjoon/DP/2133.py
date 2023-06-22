num = int(input())
DP = [0] * 31
DP[1] = 0
DP[2] = 3

for i in range(4, num+1, 2):
    DP[i] = 3*DP[i-2] + 2
    for j in range(i-4, -1, -2):
        DP[i] += DP[j]*2
    
print(DP[num])
