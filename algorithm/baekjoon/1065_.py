# https://www.acmicpc.net/problem/1065

import sys
input = sys.stdin.readline


def check(num: int):

    digits = []
    length = len(str(num))
    for i in range(length):
        digits.append(num % 10)
        num //= 10

    if arithmetic_sequence(digits):
        return 1
    else:
        return 0


def arithmetic_sequence(nums: list):

    if len(nums) < 2:
        return True

    gap = nums[1] - nums[0]
    for i in range(1, len(nums)-1):
        if nums[i+1] - nums[i] != gap:
            return False
    else:
        return True


N = int(input())

ans = 0

for i in range(1, N+1):

    ans += check(i)

print(ans)
