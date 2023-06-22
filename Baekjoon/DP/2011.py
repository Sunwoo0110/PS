num = input()
check = False

if num == "" or int(num[0]) == 0:
    check = True
    
DP = [0] * (5000)
DP[0] = 1

if len(num) >= 2 and ((int(num[0]) > 2 and int(num[1]) != 0) or (int(num[0]) == 2 and int(num[1]) > 6) or (int(num[0]) <= 2 and int(num[1]) == 0)):
    DP[1] = 1
elif len(num) >= 2 and (int(num[0]) == 1 or (int(num[0]) == 2 and int(num[1]) <= 6)):
    DP[1] = 2
elif len(num) >= 2:
    check = True
    
for i in range(2, len(num)):
    if (int(num[i-1]) > 2 and int(num[i]) != 0) or (int(num[i-1]) == 2 and int(num[i]) > 6) or  (int(num[i-1]) == 0 and int(num[i]) != 0):
        DP[i] = DP[i-1]
    elif (int(num[i-1]) == 1 and int(num[i]) != 0) or (int(num[i-1]) == 2 and int(num[i]) <= 6 and int(num[i]) != 0):
        DP[i] = DP[i-1] + DP[i-2]
    elif int(num[i-1]) != 0  and int(num[i-1]) <= 2 and int(num[i]) == 0:
        DP[i] = DP[i-2]
    else:
        check = True
        break
if check:
    print(0)
else:
    print(DP[len(num)-1]%1000000)
