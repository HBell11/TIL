# https://www.acmicpc.net/problem/10810

N, M = map(int, input().split())

boxes = [0 for _ in range(N)]

for _ in range(M):
    i, j, k = map(int, input().split())

    for idx in range(i-1, j):
        boxes[idx] = k

print(*boxes)
