# https://www.acmicpc.net/problem/10971

def recursive(depth, start_i, acc_sum):
    global min_cost, start

    if acc_sum >= min_cost:
        return

    if depth == N-1:
        # print('---')
        if costs[start_i][start]:
            acc_sum += costs[start_i][start]
            if min_cost > acc_sum:
                min_cost = acc_sum
        return

    visited[start_i] = 1

    for i in range(N):
        if not visited[i] and costs[start_i][i]:
            # print(visited)
            recursive(depth+1, i, acc_sum + costs[start_i][i])

    visited[start_i] = 0


N = int(input())

costs = tuple(tuple(map(int, input().split())) for _ in range(N))
# print(costs)
visited = [0] * N

min_cost = 987654321

for start in range(N):
    recursive(0, start, 0)

print(min_cost)
