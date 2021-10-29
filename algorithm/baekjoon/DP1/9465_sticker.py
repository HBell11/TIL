# https://www.acmicpc.net/problem/9465

for _ in range(int(input())):
    n = int(input())

    stickers = [[0] + list(map(int, input().split())) for _ in range(2)]

    # !Faster
    # s = []
    # for k in range(2):
    #     s.append(list(map(int, input().split())))
    # for j in range(1, n):
    #     if j == 1:
    #         s[0][j] += s[1][j - 1]
    #         s[1][j] += s[0][j - 1]
    #     else:
    #         s[0][j] += max(s[1][j - 1], s[1][j - 2])
    #         s[1][j] += max(s[0][j - 1], s[0][j - 2])

    # print(max(s[0][n - 1], s[1][n - 1]))

    dp = [[0] * (n+1) for _ in range(2)]

    for i in range(1, n+1):

        for k in range(2):
            if i == 1:
                dp[k][i] = stickers[k][i]
            else:
                dp[k][i] = max(dp[1-k][i-1] + stickers[k][i],
                               dp[1-k][i-2] + stickers[k][i])

    print(max(dp[0][n], dp[1][n]))

    # 아래는 왜 안되는지 모르겠네....

    #     sum_1[i] = sum_1[i-1] + stickers[chk_1][i]
    #     sum_2[i] = sum_2[i-1] + stickers[chk_2][i]

    #     chk_1 = 1-chk_1
    #     chk_2 = 1-chk_2

    #     if i == 1:
    #         continue

    #     if stickers[chk_1][i] > stickers[chk_2][i]:
    #         val = sum_1[i-2] + stickers[chk_1][i]
    #         if dp[i] < val:
    #             sum_2[i] = val
    #             dp[i] = val

    #     else:
    #         val = sum_2[i-2] + stickers[chk_2][i]
    #         if dp[i] < val:
    #             sum_1[i] = val
    #             dp[i] = val

    # # print(sum_1)
    # # print(sum_2)
    # print(dp[n])
