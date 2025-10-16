'''
문제: https://www.acmicpc.net/problem/1654
접근: SWEA 츄러스 문제, 그러나 기억나지 않음
아마 절반씩 줄이거나 늘려가며 탐색하는 이진 탐색

시간복잡도: O(KlogM) 여기서 M은 최대 랜선의 길이라고 합니다.
'''

import sys

K, N = map(int, input().split())
lines = [int(sys.stdin.readline()) for _ in range(K)]
lines.sort()


start = 1
end = max(lines)

result = 0

while start <= end:
    mid = (start + end)//2

    cnt = 0
    for line in lines:
        cnt += line//mid

    if cnt >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)