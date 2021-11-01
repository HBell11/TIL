# https://www.acmicpc.net/problem/9251

s1 = input()
s2 = input()

len_1 = len(s1)
len_2 = len(s2)

dp = [[0] * (len_2+1) for _ in range(len_1+1)]

for i in range(1, len_1+1):
    for j in range(1, len_2+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
