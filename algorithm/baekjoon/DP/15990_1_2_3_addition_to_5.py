# https://www.acmicpc.net/problem/15990
import sys
input = sys.stdin.readline

T = int(input())

n = 100000
k = 1000000009
dp = [[0] * (n+1) for _ in range(3)]

for i in range(1, n+1):
    if i == 1:
        dp[0][i] = 1
    if i == 2:
        dp[1][i] = 1
    if i == 3:
        dp[2][i] = 1

    dp[0][i] += dp[1][i-1] + dp[2][i-1]
    dp[0][i] %= k

    dp[1][i] += dp[0][max(0, i-2)] + dp[2][max(0, i-2)]
    dp[1][i] %= k

    dp[2][i] += dp[0][max(0, i-3)] + dp[1][max(0, i-3)]
    dp[2][i] %= k
    # dp[3][i] = (dp[0][i] + dp[1][i] + dp[2][i]) % 1000000009

for _ in range(T):
    j = int(input())
    print((dp[0][j] + dp[1][j] + dp[2][j]) % k)
