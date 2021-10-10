# https://www.acmicpc.net/problem/5568
from itertools import permutations

n = int(input())
k = int(input())
cards = []

for _ in range(n):
    cards.append(input())

result = []

for case in permutations(cards, k):
    # print(case)
    possible_num = ''
    for letter in case:
        possible_num += letter

    possible_num = int(possible_num)
    if possible_num in result:
        continue
    result.append(possible_num)

print(len(result))
