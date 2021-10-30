# https://www.acmicpc.net/problem/9084

for _ in range(int(input())):
    N = int(input())    # 동전 수
    coins = list(map(int, input().split()))  # 동전 종류
    M = int(input())    # 목표 금액

    dp = [0] * (M+1)
    dp[0] = 1

    for coin in coins:

        for j in range(coin, M+1):
            dp[j] += dp[j-coin]
    print(dp[M])
