tc_num = int(input())

for i in range(tc_num):
    num = int(input())
    arr = [0] * 2
    arr[0] = list(map(int, input().split()))
    arr[1] = list(map(int, input().split()))
    
    DP = [[0] * num for _ in range(2)]
    
    for b in range(num):
        for a in range(2):
            if b == 0:
                DP[a][b] = arr[a][b]
            elif b == 1:
                DP[a][b] = arr[a][b] + arr[1-a][b-1]
            else:
                DP[a][b] = arr[a][b] + max(DP[1-a][b-1], DP[1-a][b-2])
    print(max(DP[0][num-1], DP[1][num-1]))