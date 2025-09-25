'''
링크: https://www.acmicpc.net/source/98709240
접근법: N의 개수가 크지 않으므로, 완탐 돌림

시간복잡도: 계산 어렵다
'''

def func(num, idx, pl, mi, mul, div):
    global min_num, max_num
    if idx == N:
        min_num = min(min_num, num)
        max_num = max(max_num, num)
        return

    if pl:
        func(num + numbers[idx], idx + 1, pl - 1, mi, mul, div)
    if mi:
        func(num - numbers[idx], idx + 1, pl, mi - 1, mul, div)
    if mul:
        func(num * numbers[idx], idx + 1, pl , mi, mul - 1, div)
    if div:
        func(int(num / numbers[idx]), idx + 1, pl, mi, mul, div - 1)
    return

N = int(input())
numbers = list(map(int, input().split()))
opers = list(map(int, input().split()))

max_num = -21e8
min_num = 21e8

func(numbers[0], 1, opers[0], opers[1], opers[2], opers[3])

print(max_num)
print(min_num)