import sys
from itertools import combinations
sys.stdin = open('input.txt')


for tc in range(int(input())):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))

    idx_list = [n for n in range(N)]

    ans = []
    for n in range(1, N+1):
        for case in combinations(idx_list, n):
            t_sum = 0

            for val in case:
                t_sum += heights[val]

            if t_sum >= B:
                ans.append(t_sum)

    print('#{} {}'.format(tc+1, min(ans)-B))
    # break
