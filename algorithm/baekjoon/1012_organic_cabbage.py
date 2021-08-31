# https://www.acmicpc.net/problem/1012
import sys
sys.setrecursionlimit(100000)


def dfs(v):
    row = v[0]
    col = v[1]

    for d in range(4):
        new_r = row + dr[d]
        new_c = col + dc[d]
        if 0 <= new_r < N and 0 <= new_c < M:

            if grid[new_r][new_c] and not visited[new_r][new_c]:
                visited[new_r][new_c] = 1
                dfs((new_r, new_c))


T = int(input())

while T > 0:

    M, N, K = map(int, input().split())

    grid = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())

        grid[Y][X] = 1

    visited = [[0 for _ in range(M)] for _ in range(N)]

    dr = (-1, 0, 1, 0)
    dc = (0, 1, 0, -1)

    cnt = 0
    for r in range(N):
        for c in range(M):
            if grid[r][c] and not visited[r][c]:
                cnt += 1
                visited[r][c] = 1
                dfs((r, c))

    print(cnt)
    T -= 1
