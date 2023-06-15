mon, day = map(int, input().split())

month_length_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_list = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

interval = day - 1

for i in range(0, mon-1):
    interval = interval + month_length_list[i]

print(month_list[interval%7])   
