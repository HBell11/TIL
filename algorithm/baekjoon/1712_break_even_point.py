# link: https://www.acmicpc.net/problem/1712

a, b, c = map(int, input().split())


# Runtime Error
# n = 0
# while c * n <= a + b * n:
#     if c <= b:
#         n = -1
#         break
#     n += 1

if b >= c:
    n = -1
else:
    n = a // (c-b) + 1

print(n)