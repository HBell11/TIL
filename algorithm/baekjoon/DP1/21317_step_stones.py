# https://www.acmicpc.net/problem/21317

N = int(input())
jumps = [tuple(map(int, input().split())) for _ in range(N-1)]
K = int(input())

if N == 1:
    print(0)

else:
    dp = [5000] * N
    dp2 = [5000] * N
    ans = [0] * N
    dp[0] = 0
    dp2[0] = 0

    dp[1] = jumps[0][0]
    ans[1] = dp[1]
    # dp[2] = min(dp[1]+jumps[1][0], jumps[0][1])

    for i in range(2, N):
        dp[i] = min(dp[i-1] + jumps[i-1][0], dp[i-2] + jumps[i-2][1])
        # dp[i] = min(dp[i-1]+jumps[i-1][0], dp[i-2]+jumps[i-2][1])

        if i == 3:
            dp2[i] = dp2[i-3] + K

        elif i > 3:
            dp2[i] = min(dp[i-3] + K, dp2[i-2] + jumps[i-2]
                         [1], dp2[i-1] + jumps[i-1][0])

        ans[i] = min(dp[i], dp2[i])

    # print(dp)
    # print(dp2)
    print(ans[N-1])
