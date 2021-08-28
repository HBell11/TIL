T = int(input())

tc = 1
while tc <= T:
    N, M = map(int, input().split())

    grid = [input() for _ in range(N)]

    base_cnt = 0     # 하양색과 빨간색 카운트 변수

    for letter in grid[0]:  # 첫 줄은 무조건 흰색
        if letter != 'W':
            base_cnt += 1

    for letter in grid[-1]:  # 마지막 줄 빨간색
        if letter != 'R':
            base_cnt += 1

    min_cnt = (N-2) * M     # 최댓값으로 초기화. -2는 첫 줄 끝 줄 제외
    for i in range(1, N-1):     # 첫 줄과 끝 줄 제외하고 (i: 하양-파랑)
        for j in range(i+1, N):  # 조합으로 구분선 2줄 뽑기 (j: 파랑-빨강)
            tmp_cnt = 0         # 각 케이스마다 최소 갯수를 카운트
            for idx in range(1, len(grid)-1):   # 첫 줄과 끝 줄 제외하고 라인 접근

                if tmp_cnt >= min_cnt:          # 값이 이미 min_cnt 이상이면
                    break                       # 반복 중지

                if idx < i:                     # i보다 작을 때 하얀색
                    for letter in grid[idx]:
                        if letter != 'W':
                            tmp_cnt += 1
                if i <= idx < j:                # i와 j 사이일 때 파란색
                    for letter in grid[idx]:
                        if letter != 'B':
                            tmp_cnt += 1
                if idx >= j:                    # j보다 크면 빨간색
                    for letter in grid[idx]:
                        if letter != 'R':
                            tmp_cnt += 1

            if min_cnt > tmp_cnt:   # minimum 보다 작은 값이면
                min_cnt = tmp_cnt   # 갱신

    total_cnt = base_cnt + min_cnt  # 두 값을 더함

    print('#{0} {1}'.format(tc, total_cnt))
    # break
    tc += 1
