# https://www.acmicpc.net/problem/1717
import sys
input = sys.stdin.readline


def union(a, b):
    # a = parents[a]
    # b = parents[b]

    if parents[a] != parents[b]:

    pass


def get_parent(e):

    if parents[e] == e:
        return e
    else:
        p = parents[e]


n, m = map(int, input().split())

# set_list = [[n] for n in range(n+1)]
parents = {}

for n in range(n+1):
    parents[n] = n

print(parents)

for _ in range(m):

    chk, a, b = map(int, input().split())

    if not chk:     # 합집합

        union(a, b)
        # pass

        # idx1 = idx2 = 0
        # for idx, my_set in enumerate(set_list):
        #     if a in my_set:
        #         t_set = my_set
        #         idx1 = idx
        #     if b in my_set:
        #         t_set2 = my_set
        #         idx2 = idx

        # if t_set != t_set2:
        #     set_list.append(t_set | t_set2)

        #     set_list.pop(idx1)
        #     set_list.pop(idx2)

    if chk:         # 두 원소가 같은 집합인지

        # if get_parent(a) != get_parent(b):
        #     print('NO')
        # else:
        #     print('YES')
        pass

        # for my_set in set_list:
        #     if a in my_set:
        #         if b in my_set:
        #             print('YES')
        #         else:
        #             print('NO')
        #         break
