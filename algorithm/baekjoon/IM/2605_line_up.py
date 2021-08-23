# https://www.acmicpc.net/problem/2605

N = int(input())

nums = list(map(int, input().split()))
line = [1]

for idx in range(1, N):
    line.insert(nums[idx], idx+1)

line.reverse()
print(*line)
