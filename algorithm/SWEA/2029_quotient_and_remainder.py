T = int(input())
lst = []

while T > 0:
    lst.append(list(map(int, input().split())))
    T -= 1

for e in lst:
    q, r = divmod(e[0], e[1])
    print(f'#{lst.index(e)+1} {q} {r}')