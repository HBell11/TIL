N = int(input())

lst = list(map(int, input().split()))

idx = N//2
lst_sorted = sorted(lst)
print(lst_sorted[idx])
    