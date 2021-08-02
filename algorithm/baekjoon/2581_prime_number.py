# 소수의 빠른 계산을 위한 모듈
import math

m = int(input())
n = int(input())

# 소수의 총 합
my_sum = 0

# m과 n 사이에 소수가 있는 지 판별하기 위함
# 있으면 1 없으면 0
chk = 0

# m이상 n이하의 경우 반복
while m <= n:
    if m == 1:
        m += 1
        continue

    # 소수판별 2부터 루트 m까지 체크
    for i in range(2, int(math.sqrt(m))+1):
        
        # m으로 나누어 떨어지는 게 있으면
        if not m % i:
            # print('합성수: ', m)

            # 반복 종료
            break

    # 전부다 체크 했으면
    else:
        # print('소수: ', m)

        # 첫 소수인지 판별
        if not chk:

            # 첫 소수를 저장
            first_prime_num = m
            chk += 1
        
        # 총 합에 저장
        my_sum += m

    m += 1

# 소수가 있으면
if chk:
    print(my_sum)
    print(first_prime_num)

# 소수가 없으면
else:
    print(-1)