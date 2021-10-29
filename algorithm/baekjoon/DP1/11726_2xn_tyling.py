# https://www.acmicpc.net/problem/11726

n = int(input())

if n == 1:
    print(1)
else:
    dp = [1] * (n+1)

    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]

    print(dp[n] % 10007)
