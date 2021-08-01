# link: https://www.acmicpc.net/problem/2291

N = int(input())
 
i = 1
while True:
    if N <= 3 * pow(i, 2) - 3 * i + 1:
        print(i)
        break
    i += 1

# 함수로 정의해서 푸니까 시간초과
# print(func(N))