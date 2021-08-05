# https://www.acmicpc.net/problem/9020

def is_num_prime(n):

    for i in range(2, int(n**0.5)+1):
        if not n % i:
            return False
    else:
        return True

T = int(input())

while T > 0:
    n = int(input())

    std_num = n // 2

    idx = 0
    while idx < std_num:

        i, j = std_num - idx, std_num + idx

        if is_num_prime(i) and is_num_prime(j):
            print(i, j)
            break

        idx += 1

    T -= 1