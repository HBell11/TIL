# https://www.acmicpc.net/problem/20437

# TimeError
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    W = input()
    K = int(input())

    length = len(W) - 1

    dp = [[] * (length+1) for _ in range(26)]

    ans1 = 10000
    ans2 = 0

    for i in range(1, length+1):
        idx = ord(W[i-1]) - 97  # ord('a')

        dp[idx].append(i)

    if K == 1:
        ans1 = ans2 = 1

    else:
        print(dp)
        for j in range(26):
            if len(dp[j]) >= K:
                for k in range(K-1, len(dp[j])):
                    print('j, k: ', j, k)
                    tmp = dp[j][k] - dp[j][k-K+1] + 1

                    print('tmp: ', tmp)

                    ans1 = min(ans1, tmp)
                    ans2 = max(ans2, tmp)

    if ans1 == 10000:
        print(-1)
    else:
        print(ans1, ans2)

# for _ in range(T):
#     W = input()
#     K = int(input())

#     length = len(W) - 1

#     dp = [[0] * (length+1) for _ in range(26)]

#     ans1 = 10000
#     ans2 = 0

#     for i in range(1, length+1):
#         idx = ord(W[i-1]) - 97  # ord('a')

#         for j in range(26):
#             if idx == j:
#                 dp[j][i] = dp[j][i-1] + 1
#             else:
#                 dp[j][i] = dp[j][i-1]

#         if K == 1:
#             ans1 = ans2 = 1
#         else:
#             if dp[idx][i] >= K:
#                 for k in range(i-1, -1, -1):

#                     if dp[idx][i] - dp[idx][k] == K:
#                         n_length = i - k
#                         break

#                 ans1 = min(ans1, n_length)
#                 ans2 = max(ans2, n_length)

#     print(-1 if ans1 == 10000 else f'{ans1} {ans2}')
