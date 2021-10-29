# https://www.acmicpc.net/problem/2294

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

dp = [-1] * (k+1)
dp[0] = 0

for coin in coins:
    for j in range(coin, k+1):
        if dp[j-coin] != -1:
            if dp[j] == -1:
                dp[j] = dp[j-coin] + 1
            else:
                dp[j] = min(dp[j], dp[j-coin] + 1)

print(dp[k])
