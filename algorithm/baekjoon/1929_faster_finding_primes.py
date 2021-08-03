# 아직 못 풂

import math

m, n = map(int, input().split())


# Runtime Error

# while m <= n:

#     idx = 2

#     while idx <= math.sqrt(m):
#         if not (m % idx):
#             break

#         idx += 1

#     else:
#         print(m)

#     m += 1


prime_list = [True] * (n+1)
for i in range(2, int(math.sqrt((n+1)))+1):
    if prime_list[i]:
        for j in range(2*i, n+1, i):
            prime_list[j] = False
    
for idx in range(m, n+1):
    if idx > 1 and prime_list[idx]:
        print(idx)



# number_list = list(range(2, int(math.sqrt(n)) + 1))
# ans_list = list(range(m, n + 1))

# for prime in number_list:

#     for ele in ans_list:
#         if ele != prime and (not ele % prime):
#             ans_list.remove(ele)

# for ele in ans_list:
#     print(ele)