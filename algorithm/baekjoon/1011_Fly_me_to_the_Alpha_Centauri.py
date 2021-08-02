# https://www.acmicpc.net/problem/1011

T = int(input())

while T > 0:

    x, y = map(int, input().split())

    distance = y - x

    n = 1
    while True:

        if distance <= n * (n+1):

            if distance <= pow(n,2):
                ans = 2 * n - 1
            else:
                ans = 2 * n
                
            break
        n += 1

    print(ans)

    T -= 1