# https://www.acmicpc.net/problem/2941


string = input()

cnt = 0

for idx in range(len(string)):

    if string[idx] == '-':
        continue

    if string[idx] == '=':

        if string[idx-1] == 'z':

            if string[idx-2] == 'd':

                cnt -= 1

        continue

    if string[idx] == 'j':

        if string[idx-1] == 'l' or string[idx-1] == 'n':

            continue

    cnt += 1

print(cnt)
