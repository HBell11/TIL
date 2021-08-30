# https://www.acmicpc.net/problem/2477

# Unsolved

K = int(input())

field = [[] for _ in range(5)]
for _ in range(6):
    direc, dist = map(int, input().split())
    field[direc].append(dist)

# print(field)

# width = 0
# height = 0
for d in range(1, 5):
    if len(field[d]) == 1:
        if d <= 2:
            width = field[d][0]
            if d % 2:
                small_width = field[d+1][0]
            else:
                small_width = field[d-1][0]
        else:
            height = field[d][0]
            if d % 2:
                small_height = field[d+1][0]
            else:
                small_height = field[d-1][0]
    # else:
    #     if d <= 2:
    #         small_width = field[d][0]
    #     else:
    #         small_height = field[d][0]

# print(small_width, small_height)

# else:
#     if d <= 2:
#         small_width = min(field[d])
#     else:
#         small_height = min(field[d])

print((width*height - small_width*small_height)*K)
