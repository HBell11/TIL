# https://www.acmicpc.net/problem/2628

w, h = map(int, input().split())
n = int(input())
cuts = [tuple(map(int, input().split())) for _ in range(n)]

width = []
height = []

for cut in cuts:
    if cut[0] == 0:     # 가로이면
        height.append(cut[1])
    else:               # 세로이면
        width.append(cut[1])

width.sort()
height.sort()

width.append(w)
height.append(h)

max_width = width[0]
for i in range(len(width) - 1):
    check_width = width[i+1] - width[i]
    if max_width < check_width:
        max_width = check_width

max_height = height[0]
for j in range(len(height) - 1):
    check_height = height[j+1] - height[j]
    if max_height < check_height:
        max_height = check_height

print(max_width * max_height)
