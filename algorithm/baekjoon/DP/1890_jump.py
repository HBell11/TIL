# https://www.acmicpc.net/problem/1890


def jump(v):

    pass


N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]

start = (0, 0)
dp[0][0] = 1

jump(start)
