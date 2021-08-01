# https://www.acmicpc.net/problem/2775

# Recursive
# Time Error

# def func(k, n):
#     if k == 0:
#         return n
#     elif n == 1:
#         return 1

#     else:
#         return func(k-1, n) + func(k, n-1)


T = int(input())

while T > 0:

    k = int(input())
    n = int(input())

    f0 = [x for x in range(1, n+1)]

    for _ in range(k):
        for idx in range(1, n):
            f0[idx] += f0[idx-1]

    print(f0[-1])

    # Recursive result
    # print(func(k, n))

    T -= 1