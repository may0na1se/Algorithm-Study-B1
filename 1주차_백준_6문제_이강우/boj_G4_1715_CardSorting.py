'''
문제: https://www.acmicpc.net/problem/1715
접근: 힙큐 써서 작은 것부터 비교해주기

'''

import sys

from heapq import heappop, heappush

def func(cnt):
    result = 0
    while cnt < N-1:
        num = heappop(lst) + heappop(lst)
        result += num
        heappush(lst, num)

        cnt += 1
    return result

N = int(sys.stdin.readline())
lst = []

for _ in range(N):
    x = int(sys.stdin.readline())
    heappush(lst, x)

print(func(0))
