num = int(input())
DP = [x for x in range(num+1)]

for i in range(1, num+1):
    for j in range(1, i+1):
        if i < j*j:
            break
        if DP[i] > DP[i-j*j]+1:
            DP[i] = DP[i-j*j]+1
print(DP[num])