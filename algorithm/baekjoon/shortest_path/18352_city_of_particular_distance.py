# https://www.acmicpc.net/problem/18352
from collections import deque
import sys
input = sys.stdin.readline


def find_path(v):
    q = deque()
    q.append(v)

    while q:
        v = q.popleft()

        if visited[v] > K:
            return

        for w in edges[v]:
            if not visited[w]:
                visited[w] = visited[v] + 1
                q.append(w)
                if visited[v] + 1 == K and w != X:
                    ans.append(w)


N, M, K, X = map(int, input().split())

edges = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    s, e = map(int, input().split())
    edges[s].append(e)

ans = []
find_path(X)

if ans == []:
    print(-1)
else:
    print(*(sorted(ans)), sep='\n')
