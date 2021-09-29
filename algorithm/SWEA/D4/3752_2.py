# Time Error

from itertools import combinations

for tc in range(int(input())):
    N = int(input())

    marks = list(map(int, input().split()))

    possible_marks = []
    for i in range(N+1):

        for case in combinations(marks, i):

            possible_marks.append(sum(case))

    ans = len(set(possible_marks))

    print('#{} {}'.format(tc+1, ans))
    # break
