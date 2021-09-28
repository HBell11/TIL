# https://www.acmicpc.net/problem/2164
from collections import deque

N = int(input())

q = deque(i for i in range(1, N+1))
# q = deque()
# for k in range(1, N+1):

# print(q)
while len(q) > 1:
    q.popleft()
    v = q.popleft()
    q.append(v)

print(q[0])
