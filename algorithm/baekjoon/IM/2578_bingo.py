# https://www.acmicpc.net/problem/2578

bingo_grid = [list(map(int, input().split())) for _ in range(5)]
numbers_call = []

for _ in range(5):
    numbers_call.extend(list(map(int, input().split())))

# print(numbers_call)
for idx, num in enumerate(numbers_call):

    for r in range(5):
        for c in range(5):
            if bingo_grid[r][c] == num:
                bingo_grid[r][c] = 0

    cnt = 0     # 빙고 개수

    # 행 탐색
    for row in bingo_grid:
        if not any(row):
            cnt += 1

    # 열 탐색
    for col in zip(*bingo_grid):
        if not any(col):
            cnt += 1

    # 좌하향 대각 탐색
    for i in range(5):
        if bingo_grid[i][i] != 0:
            break
    else:
        cnt += 1

    # 우상향 대각 탐색
    for j in range(5):
        if bingo_grid[j][4-j] != 0:
            break
    else:
        cnt += 1

    # 빙고 개수가 3개 이상이면
    if cnt >= 3:
        print(idx+1)
        break
