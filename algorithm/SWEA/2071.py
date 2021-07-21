T = int(input())
lst = []

for i in range(T):
    lst.append(list(map(int, input().split())))

my_avgs = []

for j in range(len(lst)):
    my_sum = 0
    for k in lst[j]:
        my_sum += k
    my_avg = my_sum/len(lst[j])
    my_avgs.append(round(my_avg))

    print(f'#{j+1} {my_avgs[j]}')