# https://www.acmicpc.net/problem/15724
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (M+1) for _ in range(N+1)]

for x in range(1, N+1):
    for y in range(1, M+1):
        dp[x][y] = population[x-1][y-1] + \
            dp[x-1][y] + dp[x][y-1] - dp[x-1][y-1]

K = int(input())
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - (dp[x2][y1-1] + dp[x1-1][y2] - dp[x1-1][y1-1]))
