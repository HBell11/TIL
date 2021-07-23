T = int(input())
lst = []

for i in range(T):
    lst.append(list(map(int, input().split())))

# print(lst)

for j in lst:
    st = ''
    if j[0] > j[1]:
        st = '>'
    elif j[0] < j[1]:
        st = '<'
    else:
        st = '='

    print(f'#{lst.index(j)+1} {st}')