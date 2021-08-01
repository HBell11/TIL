# link: https://www.acmicpc.net/problem/1193

X = int(input())

i = 0
while True:

    floor_num = (pow(i, 2) + i) // 2

    if X <= floor_num:
        idx = i
        break

    prev_floor_num = floor_num
    i += 1

subidx = X - prev_floor_num

if idx & 1:
    numerator = idx + 1 - subidx
    denomenator = subidx

else:
    numerator = subidx
    denomenator = idx + 1 - subidx

print(f'{numerator}/{denomenator}')