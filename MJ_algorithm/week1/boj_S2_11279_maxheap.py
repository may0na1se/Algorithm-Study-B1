import sys
import heapq
input = sys.stdin.readline 

pq = []

N = int(input())

for _ in range(N):
    n = int(input())
    if n == 0 :
        if len(pq) == 0 :
            print(0)
        else:
            print(-1 * heapq.heappop(pq))

    else :
        heapq.heappush(pq, -n)

