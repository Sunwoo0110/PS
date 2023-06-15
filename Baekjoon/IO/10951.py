import sys

test_list = sys.stdin.readlines()

for test in test_list:
    a, b = map(int, test.split(" "))
    print(a+b)
