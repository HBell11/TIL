# https://www.acmicpc.net/problem/10157

# Unsolved

C, R = map(int, input().split())

K = int(input())

grid = [[0] * C for _ in range(R)]
direction = 0
r = c = 1

idx = 1
while idx <= C*R:

    if idx == K:
        break

    else:

        if 1 <= r <= R and 1 <= c <= C:
            if direction == 0:
                r += 1

            elif direction == 1:
                c += 1

            elif direction == 2:
                r -= 1

            else:
                c -= 1

    print(c, r)

    idx += 1

# print(c, r)
