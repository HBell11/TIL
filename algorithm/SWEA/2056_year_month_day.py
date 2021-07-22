T = int(input())
lst = []

for _ in range(T):
    lst.append(int(input()))

for i in range(len(lst)):
    chk = 0
    val = lst[i]
    y = val // 10000
    val %= 10000
    m = val // 100
    val %= 100
    d = val
    
    # month에 대한 예외사항
    if m < 1 or m > 13:
        chk = 1
    
    # day에 대한 예외사항
    if m in [4,6,9,11]:
        if d > 30:
            chk = 1
    elif m == 2:
        if d > 28:
            chk = 1
    else:
        if d > 31:
            chk = 1
    
    if chk:
        print(f'#{i+1} {-1}')
    else:
        print(f'#{i+1} {str(y).zfill(4)}/{str(m).zfill(2)}/{str(d).zfill(2)}')
