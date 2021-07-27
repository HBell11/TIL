T = int(input())

i = 1
while i <= T:

    N = int(input())
    ans_list = list(map(int, input().split()))


    ans_list.sort()

    print(f'#{i}', end = ' ')

    for e in ans_list:
        print(e, end = ' ')
    print()


    i += 1