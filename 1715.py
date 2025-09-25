import heapq

# 그리디 + 힙큐
# 가장 매수가 적은 뭉치 두개를 먼저 합치는 것이 유리

N = int(input())
q = []
for _ in range(N):
    heapq.heappush(q, int(input()))
result = 0
while q:
    card1 = heapq.heappop(q)
    # 더이상 남은 카드 묶음이 없을 경우 자동 종료
    if q:
        card2 = heapq.heappop(q)
        result += card1 + card2
        heapq.heappush(q, card1 + card2)
print(result)