# https://www.acmicpc.net/problem/16987
import sys
input = sys.stdin.readline


def recursive(idx):
    global ans

    # print('!!!!: ', idx)
    if idx == N:
        # if all(broken[idx+1:]):
        # print('final!!', idx, broken)

        if ans < sum(broken):
            ans = sum(broken)
        return

    # if all(broken[idx+1:]):
    #     recursive(N-1)
    if broken[idx] or all(broken[:idx] + broken[idx+1:]):
        recursive(idx+1)
        return

    # print('idx: ', idx)
    # print('broken: ', broken)
    for i in range(N):

        if i == idx:
            continue

        # print('i: ', i)

        if not broken[i]:

            eggs[idx][0] -= eggs[i][1]
            eggs[i][0] -= eggs[idx][1]
            check(i, idx)

            recursive(idx+1)

            eggs[idx][0] += eggs[i][1]
            eggs[i][0] += eggs[idx][1]
            check(i, idx)

    if idx == N-1:
        recursive(idx+1)


def check(a, b):

    if eggs[a][0] > 0:
        broken[a] = 0
    else:
        broken[a] = 1

    if eggs[b][0] > 0:
        broken[b] = 0
    else:
        broken[b] = 1


N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
broken = [0] * N

ans = 0
recursive(0)
print(ans)
