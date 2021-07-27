T = int(input())

i = 1
while i <= T:

    N = int(input())

    change_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    ans_list = []

    for change in change_list:
        ans_list.append(N//change)
        N %= change

    print(f'#{i}')
    for e in ans_list:
        print(e, end=' ')
    print()

    i += 1