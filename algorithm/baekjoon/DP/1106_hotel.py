# https://www.acmicpc.net/problem/1106

C, N = map(int, input().split())

data = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (C+1)

for i in range(1, C+1):

    min_d = 987654321

    for d in data:

        val = dp[max(0, i-d[1])] + d[0]
        if min_d > val:
            min_d = val

    dp[i] = min_d

print(dp[C])
