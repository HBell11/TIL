# https://www.acmicpc.net/problem/2628

# Unsolved

v, h = map(int, input().split())
n = int(input())
cuts = [list(map(int, input().split())) for _ in range(n)]

for cut in cuts:
    if cut[0] == 0:
        pass
