# https://www.acmicpc.net/problem/17609

def pal(s: str, chance):

    length = len(s)

    for i in range(length//2):
        if s[i] != s[length-(i+1)]:
            if chance:
                tmp1 = pal(s[:i] + s[i+1:], False)
                if not tmp1:
                    return 1
                tmp2 = pal(s[:length-(i+1)] + s[length-i:], False)
                if not (tmp2):
                    return 1
            return 2
    else:
        return 0


for _ in range(int(input())):
    s = input()

    print(pal(s, True))
