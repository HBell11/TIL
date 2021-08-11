def solution(n):

    cul_n = 0
    r = c = 0
    temp_list = []

    for i in range(1, n + 1):
        temp_list.append([0] * i)
        cul_n += i

    k = 1
    d = 0
    num_in_row = n
    while k <= cul_n:

        if d == 0:
            for i in range(num_in_row):
                temp_list[r + i][c] = k
                k += 1
            r += i
            c += 1

        elif d == 1:
            for i in range(num_in_row):
                temp_list[r][c + i] = k
                k += 1
            r -= 1
            c += i - 1

        else:
            for i in range(num_in_row):
                temp_list[r - i][c - i] = k
                k += 1
            r -= i - 1
            c -= i

        d = (d + 1) % 3
        num_in_row -= 1

    answer = []
    for tmp in temp_list:
        answer += tmp

    return answer


print(solution(4))
print(solution(5))
print(solution(6))
