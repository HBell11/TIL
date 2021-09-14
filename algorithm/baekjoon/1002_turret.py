# https://www.acmicpc.net/problem/1002

def distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5


T = int(input())

while T > 0:
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    p1 = (x1, y1)
    p2 = (x2, y2)

    d = distance(p1, p2)

    if d == 0:
        if r1 == r2:
            ans = -1
        else:
            ans = 0

    else:
        if d > r1 + r2:
            ans = 0
        elif d == r1+r2:
            ans = 1
        elif d < r1 + r2:
            ans = 2
            if d == abs(r1-r2):
                ans = 1
            elif d < abs(r1-r2):
                ans = 0

    print(ans)
    T -= 1
