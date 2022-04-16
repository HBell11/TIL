# https://www.acmicpc.net/problem/11729
import sys
input = sys.stdin.readline


def recursive(n, start, end):

    if n == 0:
        return

    mid = 6 - (start + end)

    recursive(n-1, start, mid)
    print(start, end)
    recursive(n-1, mid, end)
    return


N = int(input())

print(2**N - 1)

recursive(N, 1, 3)
