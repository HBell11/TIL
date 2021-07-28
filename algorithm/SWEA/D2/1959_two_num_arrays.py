T = int(input())

num_cases = 1
while num_cases <= T:

    N, M = map(int,input().split())

    # Ai 와 Bj 생성
    a_sub_i = list(map(int, input().split()))
    b_sub_j = list(map(int, input().split()))

    final_sum = 0

    if N < M:
        # 마주보는 위치의 경우의 수
        position_cases = M - N + 1

        # 경우의 수 별로 반복
        num = 0
        while num < position_cases:
            tmp_sum = 0
            for idx_a in range(N):
                tmp_sum += (a_sub_i[idx_a] * b_sub_j[idx_a + num])
            if tmp_sum >= final_sum:
                final_sum = tmp_sum
            num += 1

    else:
        position_cases = N - M + 1

        num = 0
        while num < position_cases:
            tmp_sum = 0
            for idx_b in range(M):
                tmp_sum += (a_sub_i[idx_b+num] * b_sub_j[idx_b])
            if tmp_sum >= final_sum:
                final_sum = tmp_sum
            num += 1

    # 출력하기
    print(f'#{num_cases} {final_sum}')

    num_cases += 1