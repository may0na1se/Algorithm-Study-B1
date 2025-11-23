# 접근 방법 : 이진탐색 시리즈 중 1개, 그냥 츄러스의 변주 느낌
# 풀이시간 15분
import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

l, r = 1, max(trees)

while l <= r:
    mid = (l + r) // 2
    total = 0
    for tree in trees:
        wood = tree - mid
        if wood > 0:
            total += wood
    if total >= M:
        l = mid + 1
    else:
        r = mid - 1

print(r)