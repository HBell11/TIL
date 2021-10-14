# https://www.acmicpc.net/problem/1182


def recursive(depth, my_sum, chk):
    global cnt

    if depth == N:
        if chk and my_sum == S:
            cnt += 1
        return

    recursive(depth+1, my_sum + nums[depth], 1)
    recursive(depth+1, my_sum, chk)


N, S = map(int, input().split())

nums = list(map(int, input().split()))

cnt = 0
recursive(0, 0, 0)
print(cnt)
