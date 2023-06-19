num = int(input())
arr = list(map(int, input().split()))
DP = [1] * num
inverse = [1] * num
reverse = [1] * num

for i in range(num):
    for j in range(i):
        if arr[i] > arr[j]:
            inverse[i] = max(inverse[i], inverse[j]+1)
        
for i in range(num-1, -1, -1):
    for j in range(num-1, i, -1):
        if arr[i] > arr[j]:
            reverse[i]  = max(reverse[i], reverse[j]+1)
            
for i in range(num):
    DP[i] = inverse[i] + reverse[i] - 1 
    
print(max(DP))