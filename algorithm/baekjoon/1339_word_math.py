# https://www.acmicpc.net/problem/1339
# from collections import defaultdict

N = int(input())

words = [input() for _ in range(N)]
# print(words)

words.sort(key=len, reverse=True)

print(words)

words_dict = {}
for word in words:
    print(word)
    words_dict[len(word)] = word

print(words_dict)

letter_to_number = [0 for _ in range(26)]
# letter_used = []


# num = 9
# while num >= 0:


#     num -= 1
