test_num = int(input())

for i in range(test_num):
    a, b = map(int, input().split(" "))
    print("Case #" + str(i+1) +": "+ str(a+b))