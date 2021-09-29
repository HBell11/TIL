# https://www.acmicpc.net/problem/17471

def divide(node, n, chk, my_sum):
    global ans

    # visited[node] = 1
    print('node: ', node)

    if n == 6:
        print('--------')
        if ans > abs(my_sum):
            ans = abs(my_sum)
            print(ans)
        return

    for child in G[node][1:]:
        if not visited[child]:
            # print('kkkkkkkk')
            print(visited)
            print('node: ', node)
            visited[child] = 1
            n += 1
            divide(child, n, chk, my_sum+districts[child])
            print('kkkk')
            divide(child, n, chk+1, my_sum-districts[child])
            n -= 1
            visited[child] = 0


N = int(input())

districts = [0]+list(map(int, input().split()))
G = [0]+[list(map(int, input().split())) for _ in range(N)]

ans = 99999
visited = [0 for _ in range(N+1)]
visited[1] = 1
divide(1, 0, 0, 0)    # node, n, chk, sum


print(G)
