num = int(input())
arr = list(map(int, input().split()))
DP = [0] * num
DP[0] = arr[0]

for i in range(1, num):
    DP[i] = arr[i]
    for j in range(i):
        if arr[i] > arr[j]:
            DP[i] =  max(DP[i], DP[j]+arr[i])
print(max(DP))