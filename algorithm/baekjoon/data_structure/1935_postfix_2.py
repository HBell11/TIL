# https://www.acmicpc.net/problem/1935

N = int(input())

sentence = input()

nums = []
for _ in range(N):
    nums.append(int(input()))

for idx in range(len(sentence)):
    if sentence[idx] == '*':
        pass
