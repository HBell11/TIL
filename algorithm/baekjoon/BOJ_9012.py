# link: https://www.acmicpc.net/problem/9012

import sys
input = sys.stdin.readline

n = int(input().strip())

for k in range(n):
    cnt = 0
    tf = 0
    s = input().strip()
    
    for i in range(len(s)):
        if cnt < 1 and s[i] == ')':
            tf = 1
            break
        elif s[i] == '(':
            cnt = cnt + 1
        else:
            cnt = cnt - 1

    if tf == 1:
        print('NO')
    else:
        if cnt == 0:
            print('YES')
        else:
            print('NO')
