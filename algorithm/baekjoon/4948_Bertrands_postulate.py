def func(n):
    
    ans = 0

    num_list = [True] * (2*n + 1)

    for i in range(2, int((2*n+1)**0.5) + 1):
        if num_list:
            for j in range(2*i, 2*n + 1, i):
                num_list[j] = False
    
    for idx in range(n+1, 2*n + 1):
        if idx > 1 and num_list[idx]:
            ans += 1

    return ans




    # for i in range(n+1, 2*n + 1):

    #     for j in range(2, int((2*i)**0.5)):
            
    #         if not i % j:
    #             break

    #     else:
    #         ans += 1

    # return ans

while True:
    n = int(input())

    if not n:
        break

    print(func(n))