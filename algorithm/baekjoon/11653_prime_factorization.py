n = int(input())

idx = 2

while True:

    if n == 1:
        break

    if not (n % idx):
        print(idx)
        n //= idx
        continue

    idx += 1