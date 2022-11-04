#!/usr/bin/env python3

day_of_week = 1
date = 1
list_of_days = []
for i in range(1, 32):
    if day_of_week > 7:
        day_of_week = 1
    list_of_days.append([date, day_of_week])
    date += 1
    day_of_week += 1

ans = 0
a = list(map(int, input().split()))
for day in a:
    if day > 31 or day < 1:
        print('輸入錯誤')
        exit()
    # search
    for d, d1 in list_of_days:
        if d == day and d1 == 1:
            ans += 1

print(ans)
