# https://www.acmicpc.net/problem/9095

# T = int(input())

for _ in range(int(input())):

    n = int(input())

    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    else:
        dp = [1] * (n+1)
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

        print(dp[n])
