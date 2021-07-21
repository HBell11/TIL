# link: https://www.acmicpc.net/problem/1697

import sys
from collections import deque

def seekandhide(arr, x, k):
  q = deque()
  q.append(x)

  while q:
    x = q.popleft()

    if x == k:
      return arr[x]

    for i in (x-1, x+1, x*2):
      if i >= 0 and i < N and arr[i] == 0:
        arr[i] = arr[x] + 1
        q.append(i)
    
if __name__ == "__main__":
  input = sys.stdin.readline
  n, k = map(int, input().split())
  N = 100001
  arr = [0] * N
  ans = seekandhide(arr, n, k)
  print(ans)
