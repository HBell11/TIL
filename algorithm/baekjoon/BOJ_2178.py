# link: https://www.acmicpc.net/problem/2178

from collections import deque

def bfs(x,y):

  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  q = deque()
  q.append((x,y))

  while q:
    x,y = q.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0<=nx<N and 0<=ny<M:
        
        if arr[nx][ny] == 0:
          continue

        elif arr[nx][ny] == 1:
          arr[nx][ny] = arr[x][y] + 1
          q.append((nx, ny))
      
      else:
        continue
          

  return arr[N-1][M-1]

    
if __name__ == "__main__":

  N, M = map(int, input().split())
  arr = []

  for i in range(N):
    arr.append(list(map(int, input())))

  ans = bfs(0,0)
  print(ans)
