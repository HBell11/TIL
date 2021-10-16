# https://www.acmicpc.net/problem/2579

N = int(input())

points = [0] + [int(input()) for _ in range(N)]

dp = [0] * (N+1)

dp[1] = points[1]

if N > 1:
    dp[2] = dp[1] + points[2]

for i in range(3, N+1):
    dp[i] = max(dp[i-2], dp[i-3] + points[i-1]) + points[i]

print(dp[N])
