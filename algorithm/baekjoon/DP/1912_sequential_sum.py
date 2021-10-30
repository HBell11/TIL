# https://www.acmicpc.net/problem/1912

n = int(input())
nums = list(map(int, input().split()))

dp = [0] * n

dp[0] = nums[0]
acc_sum = nums[0]

for i in range(1, n):

    acc_sum += nums[i]

    if acc_sum < 0:
        acc_sum = 0
        dp[i] = max(dp[i-1], nums[i])
        continue

    dp[i] = max(acc_sum, dp[i-1])

print(dp[n-1])
