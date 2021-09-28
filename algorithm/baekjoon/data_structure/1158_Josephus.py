# https://www.acmicpc.net/problem/1158

N, K = map(int, input().split())

nums = [i for i in range(1, N+1)]

ans = []

idx = 0

while nums:
    idx += K-1
    idx %= len(nums)
    ans.append(nums.pop(idx))

print('<', end='')
print(*ans, sep=', ', end='')
print('>')
