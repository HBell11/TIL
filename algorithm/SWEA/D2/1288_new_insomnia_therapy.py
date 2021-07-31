T = int(input())

i = 1
while i <= T:
    
    N = int(input())
    check_list = []

    j = 1
    while True:
        
        check_str = str(N * j)

        for letter in check_str:
            # print(letter)
            if letter not in check_list:
                check_list.append(letter)

        if len(check_list) == 10:
            break
            
        j += 1

    print(f'#{i} {N*j}')
    i += 1