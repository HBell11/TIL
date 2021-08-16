# https://www.acmicpc.net/problem/2635

num = int(input())


def jjab_fibonacci(n1):

    max_cnt = 0

    # 두번 째 수 탐색
    for n2 in range(n1, 0, -1):  # 처음에 n1보다 작은 양수라고 문제를 잘못 이해해서 입력이 1일 때 헤멤
        n3 = n1 - n2
        cnt = 3
        start_n2 = [n1, n2, n3]

        while n2 - n3 >= 0:
            n2, n3 = n3, n2 - n3
            cnt += 1
            start_n2.append(n3)

        if max_cnt < cnt:
            max_cnt = cnt
            n2_for_max = start_n2

    return max_cnt, n2_for_max


print(jjab_fibonacci(num)[0])
print(*jjab_fibonacci(num)[1])
