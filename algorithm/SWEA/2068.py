T = int(input())
lst = []

for i in range(T):
    lst.append(list(map(int, input().split())))

for j in lst:
    my_max = 0
    for k in range(len(j)):
        if my_max < j[k]:
            my_max = j[k]
    print(f'#{lst.index(j)+1} {my_max}')