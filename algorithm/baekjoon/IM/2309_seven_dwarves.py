# https://www.acmicpc.net/problem/2309

h_list = []

for _ in range(9):
    h_list.append(int(input()))

h_remain = sum(h_list) - 100

for idx in range(9):
    the_other_h = h_remain - h_list[idx]
    if the_other_h in h_list[idx+1:]:
        h_list.remove(h_list[idx])
        h_list.remove(the_other_h)
        h_list.sort()
        break

print(*h_list, end=' ')
