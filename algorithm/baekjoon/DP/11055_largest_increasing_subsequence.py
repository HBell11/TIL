# https://www.acmicpc.net/problem/11055

N = int(input())
nums = list(map(int, input().split()))

dp = [0] * N
acc_sum = [0] * N

dp[0] = nums[0]
acc_sum[0] = nums[0]

for i in range(1, N):

    cur_sum = 0

    for j in range(i):
        # print(i, j)

        if nums[j] < nums[i] and acc_sum[j] > cur_sum:
            cur_sum = acc_sum[j]

        # else:
        #     acc_sum = max(0, acc_sum - nums[j])

    # else:
    #     acc_sum = 0
    acc_sum[i] = cur_sum + nums[i]
    # acc_sum += nums[i] + num
    # print(i, '일 때', acc_sum)
    dp[i] = max(dp[i-1], acc_sum[i])

# print(acc_sum)
# print(dp)
print(dp[N-1])


# for i in range(1, N):

#     cur_sum = nums[i]

#     for j in range(i-1, -1, -1):
#         # print(i, j)

#         if nums[j] < nums[i] and acc_sum[j] > cur_sum:
#             # cur_sum = acc_sum[j]


#         # else:
#         #     acc_sum = max(0, acc_sum - nums[j])

#     # else:
#     #     acc_sum = 0
#     acc_sum[i] = cur_sum
#     # acc_sum += nums[i] + num
#     # print(i, '일 때', acc_sum)
#     dp[i] = max(dp[i-1], acc_sum[i])

# print(acc_sum)
# print(dp)
# print(dp[N-1])
