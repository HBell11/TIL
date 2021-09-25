# https://www.acmicpc.net/problem/10870

n = int(input())

if n == 0:
    print(0)

elif n == 1:
    print(1)

else:
    dp = []
    dp.append(0)
    dp.append(1)
    for i in range(2, n+1):
        dp.append(dp[i-2] + dp[i-1])
    print(dp[n])
