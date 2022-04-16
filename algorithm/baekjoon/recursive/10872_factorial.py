# https://www.acmicpc.net/problem/10872

N = int(input())

ans = 1

while N > 0:
    ans *= N
    N -= 1

print(ans)
