# https://www.acmicpc.net/problem/10250

import math

T = int(input())

while T > 0:
    h, w, n = map(int, input().split())

    y = n % h
    if y == 0:
        y = h
        
    x = int(math.ceil(n / h))

    print(y * 100 + x)

    T -= 1
