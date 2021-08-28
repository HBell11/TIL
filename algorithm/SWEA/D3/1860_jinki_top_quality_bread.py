T = int(input())

tc = 1
while tc <= T:
    N, M, K = map(int, input().split())     # M초에 K개
    people = list(map(int, input().split()))

    people.sort()           # 선착순 정렬

    stack = 0               # 붕어빵을 담자
    last = people[-1]       # 마지막 사람이 오는 시간

    time = 0                # 시간변수 (오픈 전에 대기타는 손님이 있네요)
    person_idx = 0          # 대기표
    while time <= last:     # 마지막 사람이 올 때 까지

        if time and not time % M:   # M 시간당 (time이 M으로 나누어떨어지면)
            stack += K              # 붕어빵 K개

        if time == people[person_idx]:  # 해당 사람이 온 시간이면
            if stack > 0:       # 붕어빵이 있는지 확인
                stack -= 1      # 붕어빵 하나를 가져가고
                person_idx += 1  # 그 다음 사람
            else:               # 붕어빵이 없으면
                ans = 'Impossible'  # 못줘요
                break

        time += 1

    else:                   # 끝 사람까지 다 팔았으면
        ans = 'Possible'

    print('#{0} {1}'.format(tc, ans))
    # break
    tc += 1
