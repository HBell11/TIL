T = int(input())
lst = []

for i in range(T):
    lst.append(list(map(int, input().split())))

my_sums = []

for j in range(len(lst)):
    my_sum = 0

    for k in lst[j]:
        if k & 1:
            my_sum += k
    my_sums.append(my_sum)

    print(f'#{j+1} {my_sums[j]}')