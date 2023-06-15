num = int(input())

for i in range(1, num+1):
    print(" "*(num - (num if i%num==0 else i%num)) + "*"*(num if i%num==0 else i%num))
    
for i in range(num-1, 0, -1):
    print(" "*(num - (num if i%num==0 else i%num)) + "*"*(num if i%num==0 else i%num))