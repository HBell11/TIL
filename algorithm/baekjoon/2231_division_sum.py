# https://www.acmicpc.net/problem/2231

N = int(input())

for num in range(N+1):
    t_num = num
    t_sum = t_num

    while t_num:
        t_sum += t_num % 10
        t_num //= 10
    
    if t_sum == N:
        print(num)
        break
else:
    print(0)