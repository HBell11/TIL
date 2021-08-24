# https://www.acmicpc.net/problem/14696
import sys
input = sys.stdin.readline

N = int(input())

while N > 0:
    a_ddakji = list(map(int, input().split()))
    b_ddakji = list(map(int, input().split()))

    a = a_ddakji.pop(0)
    b = b_ddakji.pop(0)

    a_star = a_ddakji.count(4)
    b_star = b_ddakji.count(4)

    a_circle = a_ddakji.count(3)
    b_circle = b_ddakji.count(3)

    a_nemo = a_ddakji.count(2)
    b_nemo = b_ddakji.count(2)

    a_triangle = a_ddakji.count(1)
    b_triangle = b_ddakji.count(1)

    if a_star > b_star:
        print('A')
    elif a_star < b_star:
        print('B')

    else:
        if a_circle > b_circle:
            print('A')
        elif a_circle < b_circle:
            print('B')

        else:
            if a_nemo > b_nemo:
                print('A')
            elif a_nemo < b_nemo:
                print('B')

            else:
                if a_triangle > b_triangle:
                    print('A')
                elif a_triangle < b_triangle:
                    print('B')

                else:
                    print('D')

    N -= 1
