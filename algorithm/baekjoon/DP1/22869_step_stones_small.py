# https://www.acmicpc.net/problem/22869

import sys
input = sys.stdin.readline

# First Solution

N, K = map(int, input().split())

stones = tuple(map(int, input().split()))

possible_stones = [0]

for i in range(N-1):
    for possible_stone in possible_stones:
        if K >= (i - possible_stone) * (1 + abs(stones[i] - stones[possible_stone])):
            possible_stones.append(i)
            break

if possible_stones[-1] == N-1:
    print('YES')
else:
    print('NO')

# PyPy

# dp = [5000] * N
# dp[0] = 0

# for i in range(N-1):

#     if dp[i] > K:
#         continue

#     for j in range(i+1, N):
#         result = (j - i) * (1 + abs(stones[i] - stones[j]))
#         dp[j] = min(dp[j], result)

# if dp[-1] > K:
#     print('NO')
# else:
#     print('YES')
