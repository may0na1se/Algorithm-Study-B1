import sys
import heapq
# 아마 sys 안쓰면 시간초과
# 힙큐의 기본적인 사용법
q = []
N = int(input())
for _ in range(N):
    command = int(sys.stdin.readline())
    if command:
        heapq.heappush(q, -command)
    else:
        if q:
            print(-heapq.heappop(q))
        else:
            print(0)