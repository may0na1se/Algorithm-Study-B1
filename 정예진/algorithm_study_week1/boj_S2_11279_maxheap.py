import sys
from heapq import heappop, heappush

# 처음엔 정렬 생각하고 heapify 썼다가 시간초과남
# 그래서 heappop, heappush 활용으로 변경
# 최대힙이니까 최소힙이 기본인 heapq에 - 붙여서 최대힙으로 처리

N = int(sys.stdin.readline())

arr = list()

for _ in range(N):
    order = int(sys.stdin.readline())
    
    if order == 0:
        if len(arr) == 0:
            print(0)
        else:
            ans = heappop(arr)
            print(-ans)
    
    else:
        heappush(arr, -order)
    