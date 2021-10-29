# https://www.acmicpc.net/problem/22857
# Unsolved

N, K = map(int, input().split())
nums = list(map(int, input().split()))

even_idxes = []
for idx, num in enumerate(nums):
    if not num % 2:
        even_idxes.append(idx)

if not even_idxes:
    max_len = 0
else:
    max_len = 1

    for even_idx in even_idxes:

        cnt = 1
        i = K
        while i > 0 or even_idx+(K-i+1) < N:

            if not nums[even_idx+(K-i+1)] % 2:
                cnt += 1
                continue

            else:
                i -= 1

        print(cnt)

# dp = [0] * (K+1)

# if K == 1:

#     for i in range(N):
#         if not nums[i] % 2:
#             dp[K] = 1
#             break

# else:
