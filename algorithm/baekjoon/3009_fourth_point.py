i = 3
point_list = []
ans_list = []

while i > 0:

    point_list.append(list(map(int, input().split())))

    i -= 1

for e in list(zip(*point_list))[0]:
    if list(zip(*point_list))[0].count(e) == 1:
        x = e
        break

for e in list(zip(*point_list))[1]:
    if list(zip(*point_list))[1].count(e) == 1:
        y = e
        break

print(x, y)
