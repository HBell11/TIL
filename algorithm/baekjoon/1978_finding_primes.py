# https://www.acmicpc.net/problem/1978

n = int(input())

check_list = list(map(int, input().split()))
ans = 0

for e in check_list:
    if e == 1:
        continue

    i = 2
    while i < e-1:
        if not e % i:
            # print(e)
            break
        i += 1
    else:
        ans += 1

print(ans)