# https://www.acmicpc.net/problem/11403

N = int(input())

G = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if G[i][k] and G[k][j]:
                G[i][j] = 1

for line in G:
    print(*line)
