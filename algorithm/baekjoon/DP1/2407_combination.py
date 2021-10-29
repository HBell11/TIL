# https://www.acmicpc.net/problem/2407
import sys
input = sys.stdin.readline


def comb(n, r):

    # if n == 0:
    #     dp[n][r] = 1
    #     return 1

    if r == 0 or n == r:
        dp[n][r] = 1
        return 1

    if dp[n-1][r-1] and dp[n-1][r]:
        dp[n][r] = dp[n-1][r-1] + dp[n-1][r]

    else:
        dp[n][r] = comb(n-1, r-1) + comb(n-1, r)

    return dp[n][r]


n, m = map(int, input().split())

dp = [[0] * (m+1) for _ in range(n+1)]

comb(n, m)
print(dp[n][m])
