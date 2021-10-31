# https://www.acmicpc.net/problem/12865

import sys
input = sys.stdin.readline

# Backtracking
# def backpack(depth, sum_weight, sum_val):
#     global ans

#     if depth == N:
#         if sum_weight <= K and ans < sum_val:
#             ans = sum_val
#         return

#     backpack(depth+1, sum_weight + items[depth][0], sum_val+items[depth][1])
#     backpack(depth+1, sum_weight, sum_val)


# N, K = map(int, input().split())
# items = []
# ans = 0

# for _ in range(N):
#     W, V = map(int, input().split())
#     items.append((W, V))

# backpack(0, 0, 0)  # depth, sum_weight, sum_val
# print(ans)


N, K = map(int, input().split())
items = [(0, 0)]

for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if j-items[i][0] >= 0:                      # 첫 스타트
            dp[i][j] = max(dp[i-1][j-items[i][0]] +
                           items[i][1], dp[i-1][j])
        else:                                       # 정렬된 데이터라는 보장이 X
            dp[i][j] = dp[i-1][j]

# print(dp)
print(dp[N][K])
