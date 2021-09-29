# Time Error

for tc in range(int(input())):
    N = int(input())

    marks = list(map(int, input().split()))

    # print(marks)
    possible_mark = []
    for i in range(1 << N):
        k = []
        # print(i)
        for j in range(N):
            if i & (1 << j):
                k.append(marks[j])

        possible_mark.append(sum(k))

    ans = len(set(possible_mark))

    print('#{} {}'.format(tc+1, ans))
    # break
