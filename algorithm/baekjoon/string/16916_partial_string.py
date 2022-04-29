# https://www.acmicpc.net/problem/16916

def max_pi(string: str):   # 최대 경계 길이 반환

    if len(string) == 1:
        return 0

    num = 0
    for i in range(1, (len(string)+1)//2):
        if string[:i] == string[-i:]:
            num = i
    return num


def kmp(S, P):
    moving_table = [-1] + [0] * len(P)

    for i in range(1, len(P)+1):
        moving_table[i] = max_pi(P[:i])

    i = 0
    while i < len(S)-len(P)+1:
        for j in range(len(P)):
            if S[i+j] != P[j]:
                i += j - moving_table[j]
                break
        else:
            return 1
    return 0


print(kmp(input(), input()))
