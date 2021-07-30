#####
####
# 아직 못 풂


T = int(input())

i = 1
while i <= T:

    N = int(input())
    main_array = [[0]*N]*N

    my_type = 0

    j = 1
    while j <= N*N:
        print(j)
        
        row, col = 0, 0

        # 오른쪽으로
        if my_type % 4 == 0:
            for n1 in range(N):
                if main_array[row][col+n1] == 0:
                    main_array[row][col+n1] = j
                    j += 1
                else:
                    col += n1
                    my_type += 1
                    break

        # 아래로
        elif my_type % 4 == 1:
            for n2 in range(N):
                if main_array[row+n2][col] == 0:
                    main_array[row+n2][col] = j
                    j += 1
                else:
                    row += n2
                    my_type += 1
                    break

        # 왼쪽으로
        elif my_type % 4 == 2:
            for n3 in range(N):
                if main_array[row][col-n3] == 0:
                    main_array[row][col-n3] = j
                    j += 1
                else:
                    col -= n3
                    my_type += 1
                    break

        # 위로
        else:
            for n4 in range(N):
                if main_array[row-n4][col] == 0:
                    main_array[row-n4][col] = j
                    j += 1
                else:
                    row -= n4
                    my_type += 1
                    break

    print(f'#{i}')

    # print(main_array)
    
    i += 1