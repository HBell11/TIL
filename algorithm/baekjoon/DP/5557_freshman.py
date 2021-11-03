# https://www.acmicpc.net/problem/5557

N = int(input())

nums = list(map(int, input().split()))

dp = [[0] * (len(nums)) for _ in range(21)]
dp[nums[0]][0] = 1

for i in range(1, len(nums)-1):
    for j in range(21):
        if dp[j][i-1] > 0:
            if j-nums[i] >= 0:
                dp[j-nums[i]][i] += dp[j][i-1]
            if j+nums[i] < 21:
                dp[j+nums[i]][i] += dp[j][i-1]

# print(list(zip(*dp)))
print(dp[nums[-1]][len(nums)-2])
