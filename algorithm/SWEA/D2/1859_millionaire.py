# RuntimeError
# 재귀를 사용해서 구현

# def max_return(lst):
    
#     ans = 0
#     n = len(lst)
#     idx = lst.index(max(lst))

#     if n == 0:
#         return None

#     if n - 1 == idx:

#         while n > 0:
#             ans += max(lst) - lst[n-1]
#             n -= 1

#         return ans

#     else:
#         former_lst = lst[:idx + 1]
#         latter_lst = lst[idx + 1:]
#         return max_return(former_lst) + max_return(latter_lst)


# T = int(input())

# while T > 0:
#     N = int(input())
#     my_list = list(map(int, input().split(' ')))[::-1]
#     print(my_list)
#     ans = max_return(my_list)
#     print(f'#{4-T} {ans}')
#     T -= 1


# RuntimeError
# while문 사용해서 구현

# T = int(input())
# while T > 0:
#     N = int(input())
#     my_list = list(map(int, input().split()))
#     my_list = my_list[::-1]
#     max_num = my_list[0]
#     my_sum = 0

#     for i in range(1, len(my_list)):
#         if max_num > my_list[i]:
#             my_sum += max_num - my_list[i]
#         else:
#             max_num = my_list[i]

#     print('#{} {}'.format(len(my_list) - T + 1, my_sum))
#     T -= 1


# for문을 사용해서 구현

T = int(input())
for j in range(T):
    N = int(input())
    my_list = list(map(int, input().split()))
    my_list = my_list[::-1]
    max_num = my_list[0]
    my_sum = 0

    for i in range(1, len(my_list)):
        if max_num > my_list[i]:
            my_sum += max_num - my_list[i]
        else:
            max_num = my_list[i]

    print('#{} {}'.format(j+1, my_sum))