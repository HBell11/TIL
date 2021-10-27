# https://www.acmicpc.net/problem/11660
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

G = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (N+1) for _ in range(N+1)]

for row in range(N):
    for col in range(N):
        dp[row+1][col+1] = G[row][col] + \
            (dp[row+1][col] + dp[row][col+1] - dp[row][col])

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = dp[x2][y2] - (dp[x2][y1-1] + dp[x1-1][y2] - dp[x1-1][y1-1])
    print(ans)
