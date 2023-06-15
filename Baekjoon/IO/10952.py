import sys

test_list = sys.stdin.readlines()

for test in test_list:
    a, b = map(int, test.split(" "))
    
    if a == 0 and b == 0:
        break
    
    print(a+b)