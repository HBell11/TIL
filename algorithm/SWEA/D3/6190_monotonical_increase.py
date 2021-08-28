def is_monotonical_number(num):

    new_num = 10            # 지금 digit이랑 비교하기 위한 대상 숫자 (가장 큰 값인 10으로 초기화)

    while num > 0:          # 자릿수 전체 순회
        digit = num % 10    # 일의 자리부터 하나씩
        if new_num >= digit:    # 이전의 digit이 지금 digit보다 더 커야지 단조증가
            num //= 10          # 일의자리를 떼어냄
            new_num = digit     # 지금 digit을 비교대상으로 저장
        else:               # 한번이라도 아니면
            return False    # False

    return True             # while문을 다 돌았으면 True


T = int(input())

tc = 1
while tc <= T:
    N = int(input())
    nums = list(map(int, input().split()))

    max_num = -1        # 단조 증가수가 없으면 -1 반환이라서 -1로 초기화
    for i in range(N-1):  # 하나씩 탐색
        for j in range(i+1, N):  # i보다 큰 다음 인덱스 j
            mul_num = nums[i]*nums[j]   # 곱해봐용
            if is_monotonical_number(mul_num):  # 곱한 숫자가 단조 증가 수이면
                if max_num < mul_num:   # 지금까지 구한 최대값보다 큰 지 확인해보고
                    max_num = mul_num   # 더 크면 값을 바꿔줍니다

    print('#{0} {1}'.format(tc, max_num))
    # break
    tc += 1
