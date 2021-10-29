# https://www.acmicpc.net/problem/1463

N = int(input())

dp = [0] * (N+1)
dp[1] = 0

for i in range(2, N+1):

    min_val = dp[i-1]+1
    if not i % 3:
        min_val = min(min_val, dp[i//3] + 1)

    if not i % 2:
        min_val = min(min_val, dp[i//2] + 1)

    dp[i] = min_val

print(dp[N])
