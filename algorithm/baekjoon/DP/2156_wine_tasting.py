# https://www.acmicpc.net/problem/2156

n = int(input())

wines = [0]
for _ in range(n):
    wines.append(int(input()))

dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] = max(dp[i-1], dp[max(0, i-3)] + wines[i-1] +
                wines[i], dp[max(0, i-2)] + wines[i])

print(dp[n])
