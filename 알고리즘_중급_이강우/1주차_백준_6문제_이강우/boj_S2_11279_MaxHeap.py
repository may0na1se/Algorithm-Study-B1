'''
링크: https://www.acmicpc.net/problem/11279
접근법: 최대힙 만들어서, 출력해주기

시간복잡도: O(logN)
'''

import sys

from heapq import heappush, heappop

N = int(sys.stdin.readline())
pq = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if not x:
        if not pq:
            print(0)
        else:
            print(-heappop(pq))
    else:
        heappush(pq, -x)