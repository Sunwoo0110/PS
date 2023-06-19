num = int(input())
arr = list(map(int, input().split()))
DP = [-1000] * num
DP[0] = arr[0]
tmp = 0

for i in range(1, num):
    DP[i] = max(DP[i-1]+arr[i], arr[i])
print(max(DP))