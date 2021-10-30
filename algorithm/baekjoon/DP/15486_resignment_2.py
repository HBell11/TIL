# https://www.acmicpc.net/problem/15486
import sys
input = sys.stdin.readline

N = int(input())
data = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (N+1)

for i in range(1, N+1):

    n_idx = i + data[i-1][0] - 1

    if n_idx < N+1:
        dp[n_idx] = max(dp[n_idx], dp[i-1] + data[i-1][1])

    dp[i] = max(dp[i], dp[i-1])

print(dp[N])
