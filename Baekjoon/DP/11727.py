num = int(input())
DP = [0] * (1000+1)
DP[1] = 1
DP[2] = 3

def findAll(n):
    for i in range(3, n+1):
        DP[i] = 2 * DP[i-2] + DP[i-1]
    return DP[n]

print(findAll(num)%10007)