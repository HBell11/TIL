# https://www.acmicpc.net/problem/1890


# def jump(v):

#     val = G[v[0]][v[1]]

#     if val == 0:
#         return

#     n_row = v[0] + val
#     n_col = v[1] + val

#     if n_row < N:
#         dp[n_row][v[1]] += 1
#         jump((n_row, v[1]))

#     if n_col < N:
#         dp[v[0]][n_col] += 1
#         jump((v[0], n_col))


def jump(v):

    row = v[0]
    col = v[1]

    val = G[row][col]

    if val == 0:
        return

    if row + val < N:
        dp[row+val][col] += dp[row][col]

    if col + val < N:
        dp[row][col+val] += dp[row][col]


N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]

start = (0, 0)
dp[0][0] = 1

for r in range(N):
    for c in range(N):
        jump((r, c))

print(dp[N-1][N-1])
