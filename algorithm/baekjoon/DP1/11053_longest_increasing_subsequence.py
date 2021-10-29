# https://www.acmicpc.net/problem/11053

N = int(input())
nums = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):

    max_dp = 0
    for j in range(i):
        if nums[j] >= nums[i]:
            continue

        if dp[j] > max_dp:
            max_dp = dp[j]

    dp[i] = max_dp + 1

print(max(dp))
# print(dp)
