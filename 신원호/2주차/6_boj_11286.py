import sys
import heapq

# 힙큐

N = int(input())
q = []
for _ in range(N):
    command = int(sys.stdin.readline())
    # 정수의 절댓값과 원본을 tuple로 저장
    # 절댓값이 같은 경우 음수가 먼저 pop 되므로 조건 만족
    if command:
        heapq.heappush(q, (abs(command), command))
    else:
        if q:
            value = heapq.heappop(q)
            print(value[1])
        else:
            print(0)