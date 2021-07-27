T = int(input())

i = 1
while i <= T:

    h1, m1, h2, m2 = map(int, input().split())

    m = (m1 + m2) % 60
    add_h = (m1 + m2) // 60

    h = (h1 + h2 + add_h) % 12

    if h == 0:
        h = 12

    print(f'#{i} {h} {m}')

    i += 1