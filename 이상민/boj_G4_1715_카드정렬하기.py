from heapq import heappush, heappop

N = int(input())
pq = []
for _ in range(N):
    heappush(pq,int(input()))

res = 0
for _ in range(N-1):
    a,b = heappop(pq),heappop(pq)
    res += a+b
    heappush(pq,a+b)

print(res)