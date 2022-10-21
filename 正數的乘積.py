a = list(map(int, input().split(",")))

num = 1
for i in a:
    if i > 0:
        num *= i
print(num if num != 1 else "000000")
