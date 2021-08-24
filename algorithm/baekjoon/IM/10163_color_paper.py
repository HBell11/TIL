# https://www.acmicpc.net/problem/10163
import sys
input = sys.stdin.readline

N = int(input())

grid_size = 1001
grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
color_cnt = [0] * (N+1)

idx = 1
while idx <= N:
    x_coord, y_coord, w, h = map(int, input().split())

    cnt = 0
    for y in range(h):
        for x in range(w):
            new_r = grid_size-1-y_coord-y
            new_c = x_coord+x

            if grid[new_r][new_c] != 0:
                color_cnt[grid[new_r][new_c]] -= 1

            grid[new_r][new_c] = idx
            cnt += 1

    color_cnt[idx] = cnt
    idx += 1

for i in range(1, N+1):
    print(color_cnt[i])
