# https://www.acmicpc.net/problem/1010

def comb(n: int, r: int):

    if dp[n][r]:
        return dp[n][r]

    if n == r or not r:
        dp[n][r] = 1
        return 1

    if r == 1:
        dp[n][r] = n
        return n

    dp[n][r] = comb(n-1, r) + comb(n-1, r-1)
    return dp[n][r]


T = int(input())

for _ in range(T):

    N, M = map(int, input().split())

    dp = [[0] * (N+1) for _ in range(M+1)]

    print(comb(M, N))
