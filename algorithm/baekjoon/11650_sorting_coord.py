# https://www.acmicpc.net/problem/11650
import sys

N = int(sys.stdin.readline())

coord_list = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    coord_list.append([x, y])

coord_list.sort(key=lambda k: (k[0], k[1]))

for i in range(N):
    print(*coord_list[i])
