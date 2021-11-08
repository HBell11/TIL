# https://www.acmicpc.net/problem/17413

S = input()

chk = True
s = ''
t_s = ''
for letter in S:
    if letter == '<':
        s += t_s + letter
        t_s = ''
        chk = False
        continue
    elif letter == '>':
        s += letter
        chk = True
        continue

    if chk:
        if letter == ' ':
            s += t_s + ' '
            t_s = ''
        else:
            t_s = letter + t_s
    else:
        s += letter
else:
    s += t_s
print(s)
