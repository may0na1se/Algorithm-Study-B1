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

for i in range(N):
    if i == 0:
        heappush(distance, -locations[i])

    if i == len(locations) - 1:
        heappush(distance, -(L - locations[i]))
        continue
  
    heappush(distance, -(locations[i+1] - locations[i]))

print(locations)
print(distance)

while M:
    max_dist = (-1) * heappop(distance)
    
    dist1 = max_dist // 2
    dist2 = max_dist - dist1

    heappush(distance, -dist1)
    heappush(distance, -dist2)

    M -= 1

print(distance)
print(-distance[0])
