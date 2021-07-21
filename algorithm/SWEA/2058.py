N = int(input())

my_sum = 0

while N > 0:
    my_sum += (N % 10)
    N //= 10
print(my_sum)