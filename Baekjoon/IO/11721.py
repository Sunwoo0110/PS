str_list = input()
tmp = ""

for i in range(len(str_list)):
    
    if i % 10 == 0 and i != 0:
        print(tmp)
        tmp = ""
        
    if i == len(str_list)-1:
        tmp = tmp + str_list[i]
        print(tmp)
    tmp = tmp + str_list[i]
    