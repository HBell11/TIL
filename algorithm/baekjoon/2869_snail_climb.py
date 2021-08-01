# https://www.acmicpc.net/problem/2869

import math
a, b, v = map(int, input().split())

one_day_up = a - b

d_day_before_height = v - a

print(int(math.ceil(d_day_before_height / one_day_up)) + 1)



# Runtime Error
# days = 0
# up = 0

# while True:
#     days += 1
#     up += a

#     if up >= v:
#         break

#     up -= b

# print(days)
