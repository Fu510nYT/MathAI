day = int(input())
if day > 31 or day < 1:
    print("輸入錯誤")

num = 0
a = {"1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六", "7":"天"}
'''
for date in range(1, 32):
    if num >= 7:
        num = 0
    num += 1
    print(date, num)
    #if date == day:
    print(f"星期{a[str(num)]}")
'''
print(f"星期{a[str(day % 7)]}")