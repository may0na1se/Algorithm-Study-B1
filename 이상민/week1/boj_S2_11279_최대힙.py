from heapq import heappop, heappush
import sys
input = sys.stdin.readline

pq = []
N = int(input())
for _ in range(N):
    n = int(input())
    if n: heappush(pq,-n)
    else:
        if pq: print(-heappop(pq))
        else:print(0)