# boj 2805 나무 자르기
# 이분 탐색

import sys
N, M = map(int, input().split())
trees = list(map(int, sys.stdin.readline().split()))
trees.sort()
lower = 0
upper = trees[-1]
result = 0
while lower <= upper:
    mid = (lower + upper) // 2
    temp = sum((tree - mid) for tree in trees if tree > mid)
    if temp >= M:
        result = mid
        lower = mid + 1
    else:
        upper = mid - 1

print(result)