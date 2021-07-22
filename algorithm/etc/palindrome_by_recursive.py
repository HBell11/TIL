def func(word, i = 0, drow = ''):
    
    if len(word) == len(drow):
        if word == drow:
            return True
        else:
            return False

    else:
        drow += word[-(i+1)]

        return func(word, len(drow), drow)

print(func('abcddcba'))