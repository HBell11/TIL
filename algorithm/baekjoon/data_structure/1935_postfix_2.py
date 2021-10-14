# https://www.acmicpc.net/problem/1935

N = int(input())

sentence = input()

nums = {}
for i in range(N):
    nums[chr(i + ord('A'))] = int(input())

tmp = []
for idx in range(len(sentence)):
    char = sentence[idx]

    if char == '*':
        b = tmp.pop()
        a = tmp.pop()
        tmp.append(a*b)

    elif char == '+':
        b = tmp.pop()
        a = tmp.pop()
        tmp.append(a+b)

    elif char == '/':
        b = tmp.pop()
        a = tmp.pop()
        tmp.append(a/b)

    elif char == '-':
        b = tmp.pop()
        a = tmp.pop()
        tmp.append(a-b)

    else:
        tmp.append(nums[char])

print('{:.2f}'.format(*tmp))
