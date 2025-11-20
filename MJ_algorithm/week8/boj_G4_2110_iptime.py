import sys


sys.stdin = open('input.txt', 'r', encoding='utf-8-sig')
input = sys.stdin.readline

N, C = map(int, input().split())

house = [int(input()) for _ in range(N)]
house.sort()
# print(house)


left = 1
right = house[-1] - house[0]

while left <= right :
    dist =  (left + right) // 2  #그냥 극단적인 값에도 실행 속도 어느정도 보장될 것 같아서 절반으로 잡았음

    last_house = house[0]
    iptime_count = 1

    for i in range(1, N):
        if house[i] - last_house >= dist :
            iptime_count += 1 
            last_house = house[i]

    if iptime_count >= C: #현재 간격에 대해서 공유기 설치가 C개 이상 가능하다면? 공유기 간격을 더 늘려봐도됨
        left = dist + 1
    else:
        right = dist - 1
    # print(dist, iptime_count)

print(dist)
