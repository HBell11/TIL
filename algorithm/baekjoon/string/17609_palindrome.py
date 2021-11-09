# https://www.acmicpc.net/problem/17609

def pal(s: str, chance):

    length = len(s)

    for i in range(length//2):
        if s[i] != s[-(i+1)]:
            if chance:
                print(s[:i] + s[i+1:])
                tmp1 = pal(s[:i] + s[i+1:], False)
                if not tmp1:
                    return 1

                print(s[:-i-1] + s[-i:])
                tmp2 = pal(s[:-(i+1)] + s[-i:], False)
                if not (tmp2):
                    return 1
            else:
                return 2
    else:
        return 0


T = int(input())

for _ in range(T):
    s = input()

    print(pal(s, True))
