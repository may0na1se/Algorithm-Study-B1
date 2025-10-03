import sys
input = sys.stdin.readline

from heapq import heappop, heappush

pq = []
N = int(input())
for _ in range(N):
    a = int(input())
    if a:
        heappush(pq,(abs(a),a))
    else:
        if pq:
            print(heappop(pq)[1])
        else:
            print(0)