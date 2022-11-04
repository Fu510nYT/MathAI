#!/usr/bin/env python3
a = list(map(int, input().split()))
ans = 0
for i in a:
    if i % 11 == 0:
        ans += i
print(ans)
