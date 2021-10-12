import sys
sys.stdin = open('input.txt')

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)


def dfs(v, distance):
    global ans, start, starting

    row = v[0]
    col = v[1]

    if ans < distance:
        start = starting
        ans = distance

    elif ans == distance:
        start = min(start, starting)

    for d in range(4):
        n_row = row + dr[d]
        n_col = col + dc[d]

        if 0 <= n_row < N and 0 <= n_col < N:
            if G[n_row][n_col] == G[row][col] + 1:
                dfs((n_row, n_col), distance+1)


for tc in range(int(input())):
    N = int(input())
    G = [list(map(int, input().split())) for _ in range(N)]

    start = 9999
    ans = 0
    for row in range(N):
        for col in range(N):
            starting = G[row][col]
            dfs((row, col), 1)

    print('#{} {} {}'.format(tc+1, start, ans))
    # break
