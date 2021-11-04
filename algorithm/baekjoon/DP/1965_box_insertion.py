# https://www.acmicpc.net/problem/1965

n = int(input())
boxes = list(map(int, input().split()))

acc = [1] * n
dp = [1] * n
# acc[0] = 1
# dp[0] = 1

for i in range(1, n):

    for j in range(i):
        if boxes[i] > boxes[j]:
            acc[i] = max(acc[i], acc[j]+1)

    dp[i] = max(dp[i-1], acc[i])


# print(acc)
print(dp)
print(dp[-1])
