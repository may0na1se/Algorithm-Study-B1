N = int(input())

import heapq

q = []

for _ in range(N):
    heapq.heappush(q, int(input()))

comparison_count = 0


if N == 1 :
    print(0)
else:
    while True:
        a = heapq.heappop(q)
        b = heapq.heappop(q)
    
    
        #10 20 30 40 50 60
        #10+20
        #10+20+30
    
        comparison_count += a+b
        new_cardpack = a+b
    
        heapq.heappush(q, new_cardpack)
    
        if len(q) == 1 :
            break
    
    print(comparison_count)