T = 10

tc = 1
while tc <= T:

    int(input())
    data = input()
    # print(data)

    stack1 = []
    string = ''
    for char in data:
        if char.isnumeric():
            string += char
        else:
            if stack1:
                string += stack1.pop()
            stack1.append(char)

    while stack1:
        string += stack1.pop()
    # print(string)

    stack2 = []

    for letter in string:
        if letter.isnumeric():
            stack2.append(int(letter))
        else:
            n1 = stack2.pop()
            n2 = stack2.pop()
            stack2.append(n1+n2)

    ans = stack2.pop()
    print(f'#{tc} {ans}')
    # break
    tc += 1
