dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)


def start(depth, v, string: str):
    global possible_nums

    if depth == 7:
        possible_nums.append(string)
        return

    row = v[0]
    col = v[1]
    string += G[row][col]

    for d in range(4):
        n_row = row + dr[d]
        n_col = col + dc[d]

        if 0 <= n_row < 4 and 0 <= n_col < 4:
            start(depth+1, (n_row, n_col), string)


for tc in range(int(input())):
    G = [tuple(map(str, input().split())) for _ in range(4)]

    possible_nums = []
    for r in range(4):
        for c in range(4):
            start(0, (r, c), '')

    print('#{} {}'.format(tc+1, len(set(possible_nums))))
    # break
