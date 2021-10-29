# https://www.acmicpc.net/problem/10844

N = int(input())

dp = [0] * (N+1)
dp[1] = 9
last_number = [0] + [1] * 9

for i in range(2, N+1):
    dp[i] = dp[i-1] * 2 - (last_number[0] + last_number[9])
    t_last_number = [0] * 10

    for j in range(9):
        t_last_number[j+1] += last_number[j]
    for k in range(1, 10):
        t_last_number[k-1] += last_number[k]

    last_number = t_last_number

print(dp[N] % 1000000000)
