# link: https://www.acmicpc.net/problem/1303

import sys
from collections import deque

def bfs(arr, x, y, s):

  visited[x][y] = True 

  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  count = 1

  q = deque()
  q.append((x,y))

  while q:
    x,y = q.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0<=nx<M and 0<=ny<N:
        
        if visited[nx][ny] == False and arr[nx][ny] == s:
          visited[nx][ny] = True
          q.append((nx, ny))
          count += 1

  return count**2

if __name__ == "__main__":
  input = sys.stdin.readline
  N, M = map(int, input().split())
  arr = [list(input().strip()) for i in range(M)]
  visited = [[False]*N for _ in range(M)]

  w_score = 0
  b_score = 0

  for i in range(M):
    for j in range(N):
      if visited[i][j] == False:
        if arr[i][j] == 'W':
          w_score += bfs(arr,i,j,'W')
        elif arr[i][j] == 'B':
          b_score += bfs(arr,i,j,'B')

  print(w_score, b_score)
