'''
문제: https://www.acmicpc.net/problem/1477
접근:

시간복잡도: 
'''

# 가장 긴 구간을 절반이 아니라, N개로 나눌 수도 있다
# 관건은 안 나눠떨어지는 애들을 어떻게 받아줘야 할까
# DP or Heapq 이용한 greedy

from heapq import heappop, heappush

N, M, L = map(int, input().split())

locations = sorted(list(map(int, input().split())))

distance = []

if N == 0:  # N == 0인 경우는 for 문으로 휴게소 간 거리를 잴 수가 없음!
    heappush(distance, (-L, -L, 1))
else:
    for i in range(N):
        if i == 0:
            heappush(distance, (-locations[i], -locations[i], 1))

        if i == len(locations) - 1:
            heappush(distance, (-(L - locations[i]), -(L - locations[i]), 1))
            continue
    
        heappush(distance, (-(locations[i+1] - locations[i]), -(locations[i+1] - locations[i]), 1))

# print(locations)
# print(distance)

while M:
    max_dist, original, divided = heappop(distance)
    divided += 1

    dist = original // divided  # 음수 양수 // 계산 차이 조심

    heappush(distance, (dist, original, divided))

    M -= 1

# print(distance)
print(-distance[0][0])
