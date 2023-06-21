num = int(input())
arr = [0] * num
DP = [0] * num

for i in range(num):
    arr[i] = int(input())
    
for i in range(num):
    if i == 0:
        DP[i] = arr[i]
    elif i == 1:
        DP[i] = DP[i-1]+arr[i]
    elif i == 2:
        DP[i] = max(arr[i] + arr[i-1], arr[i] + arr[i-2])
    else:
        DP[i] = max((DP[i-3]+arr[i-1]+arr[i]), (DP[i-2]+arr[i]))
    
print(DP[num-1])