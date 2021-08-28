# Unsolved

T = int(input())

tc = 1
while tc <= T:
    N, M = map(int, input().split())

    grid = []
    for _ in range(N):
        grid.append(input())

    # print(grid)

    cnt = 0

    for idx, line in enumerate(grid):
        if idx == 0:                # 첫 줄
            for letter in line:
                if letter != 'W':
                    cnt += 1

        if idx == N - 1:            # 마지막 줄
            for letter in line:
                if letter != 'R':
                    cnt += 1

    # color = 0
    # for line in grid:
    #     if color == 0:
    #         for letter in range(M):
    #             if letter != 'W':
    #                 cnt += 1
    #         color = 1
    #         continue

    #     if color == 1:
    #         white = line.count('W')
    #         blue = line.count('B')
    #         if white >= blue:
    #             for letter in range(M):
    #                 if letter != 'W':
    #                     cnt += 1
    #         else:
    #             for letter in range(M):
    #                 if letter != 'B':
    #                     cnt += 1
    #             color = 2
    #         continue

    #     if color == 2:
    #         blue = line.count('B')
    #         red = line.count('R')
    #         if blue >= red:
    #             for letter in range(M):
    #                 if letter != 'B':
    #                     cnt += 1
    #         else:
    #             for letter in range(M):
    #                 if letter != 'R':
    #                     cnt += 1
    #             color = 3
    #         continue

    #     if color == 3:
    #         for letter in range(M):
    #             if letter != 'R':
    #                 cnt += 1
    #         continue

            # print(white, blue)

    print('#{0} {1}'.format(tc, cnt))
    break
    tc += 1
