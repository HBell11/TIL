
## 아직 못 풂

N = int(input())

i = 1
while i <= N:
    decoded_str = ''

    st = 'Man'
    six_bit_cnt_list = []

    for s in st:
        k = ord(s)
        
        print(k)
        temp_k = []
        check_k = []

        while k > 0:
            if k < 2:
                temp_k.append(k)
            else:
                temp_k.append(k%2)
            k //= 2
        
        if len(temp_k) < 8:
            j = 0
            while j <  8 - len(temp_k):
                temp_k.append(0)
                j += 1
        temp_k = temp_k[::-1]

        # print(temp_k)
        # print(binary_k)
        six_bit_cnt_list.extend(temp_k)

    print(six_bit_cnt_list)
    for idx in range(0,len(six_bit_cnt_list),6):
        tmp_str = six_bit_cnt_list[idx:idx+6]
        ascii_list = []
        binary_to_decimal_list = []

        binary_e = 0
        while binary_e < 6:
            binary_to_decimal_list.append(pow(2, binary_e) * tmp_str[5-binary_e])
            binary_e += 1

        ascii_num = sum(binary_to_decimal_list)

        A_ascii = ord('A')




        # print(ascii_num)
        # print(ascii_num)
        # decoded_str += chr(ascii_num)

    # print(decoded_str)
        # chr((binary_k))




    

    

    print(f'#{i} {decoded_str}')
    i += 1