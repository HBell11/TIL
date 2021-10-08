for tc in range(int(input())):
    binaried = input()
    ternaried = input()

    possible_nums = []
    for idx in range(len(binaried)):
        for possible_letter in range(2):
            k = str(possible_letter)
            if k != binaried[idx]:
                fixed_binary = binaried[:idx] + k + binaried[idx+1:]
                num = int(fixed_binary, 2)
                possible_nums.append(num)

    ans = 0
    for idx2 in range(len(ternaried)):
        if ans:
            break

        for possible_letter in range(3):
            k = str(possible_letter)
            if k != ternaried[idx2]:
                fixed_ternary = ternaried[:idx2] + k + ternaried[idx2+1:]
                num = int(fixed_ternary, 3)
                if num in possible_nums:
                    ans = num
                    break

    print('#{} {}'.format(tc+1, ans))
    # break
