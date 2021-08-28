T = 10

tc = 1
while tc <= T:
    N = int(input())

    table = []
    for _ in range(N):
        table.append(list(map(int, input().split())))

    table_zip = zip(*table)     # 테이블을 전치시켜서 생각 (가로줄로 접근하는게 편할 것 같아서)

    cnt = 0                     # 총 교착상태 수를 담을 변수
    for line in table_zip:      # 한 줄씩 접근
        chk = 0                 # 지금 붉은 자성체가 움직이고 있는지 판단할 변수
        for element in line:    # 한 줄에서 하나씩 요소 접근
            if element == 1:    # 요소가 붉은 자성체이면
                chk = 1         # 움직이기 시작 (붉은 자성체를 여러번 만나도 1로 고정)
            if chk and element == 2:    # 붉은 자성체가 움직이고 있는데 2를 만나면
                cnt += 1        # 교착상태 +1
                chk = 0         # 붉은 자성체 다시 안움직임

    print('#{0} {1}'.format(tc, cnt))
    # break
    tc += 1
