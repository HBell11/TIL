# https://www.acmicpc.net/problem/2669
# from pandas import DataFrame


grid_check = [[0] * 100 for _ in range(100)]        # 색칠할 그리드 판

rectangles = [list(map(int, input().split())) for _ in range(4)]

for rectangle in rectangles:        # 직사각형 4개를 순회
    for x in range(rectangle[0], rectangle[2]):     # x좌표
        for y in range(rectangle[1], rectangle[3]):  # y좌표
            if grid_check[x][y] == 0:               # 아직 비어있으면
                grid_check[x][y] = 1                # 색칠

# print(DataFrame(grid_check))      # 시각적으로 확인하기 위함
cnt = 0
for x in range(100):
    for y in range(100):
        if grid_check[x][y] == 1:
            cnt += 1

print(cnt)
