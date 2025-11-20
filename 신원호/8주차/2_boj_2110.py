# boj 2110 공유기 설치
# 이분 탐색

import sys

N, C = map(int, sys.stdin.readline().split())
houses = [int(sys.stdin.readline()) for _ in range(N)]
houses.sort()
distances = [houses[i + 1] - houses[i] for i in range(N - 1)]


def able(limit_distance, router):
    cnt = 1
    check = 0
    for distance in distances:
        check += distance
        if check >= limit_distance:
            cnt += 1
            check = 0
            if cnt >= router:
                return True

    return False


lower = min(distances)
upper = houses[-1] - houses[0]

while lower <= upper:
    mid = (lower + upper) // 2
    if able(mid, C):
        lower = mid + 1
    else:
        upper = mid - 1

print(upper)