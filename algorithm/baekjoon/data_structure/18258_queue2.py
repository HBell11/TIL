# https://www.acmicpc.net/problem/18258
import sys
input = sys.stdin.readline

N = int(input())
q = [0 for _ in range(N)]
front = rear = -1

for _ in range(N):
    input_str = input().split()
    con = input_str[0]

    if con == 'push':
        rear += 1
        q[rear] = int(input_str[1])

    elif con == 'pop':
        front += 1
        k = q[front]
        if k:
            print(k)
            q[front] = 0
        else:
            print(-1)
            front -= 1

    elif con == 'size':
        print(rear - front)

    elif con == 'empty':
        if rear == front:
            print(1)
        else:
            print(0)

    elif con == 'front':
        if q[front+1]:
            print(q[front+1])
        else:
            print(-1)

    elif con == 'back':
        if q[rear]:
            print(q[rear])
        else:
            print(-1)
