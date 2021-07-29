T = int(input())

i = 1
while i <= T:

    N = int(input())
    prime_list = [2, 3, 5, 7, 11]

    e_list = [0, 0, 0, 0, 0]

    n = 0

    while n < len(e_list):
        if not (N % prime_list[n]):
            N //= prime_list[n]
            e_list[n] += 1
            continue
        n += 1
        
    ans_str = ' '.join(map(str, e_list))
    
    print(f'#{i} {ans_str}')
    i += 1