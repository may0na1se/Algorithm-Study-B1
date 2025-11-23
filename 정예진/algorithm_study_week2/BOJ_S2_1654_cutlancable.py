# 접근 방법 : 상민이의 츄러스 by KKR과 동일한 문제
# 이진 탐색 - N개 이상 나오는 최대 길이를 구하는 것이 목표이므로 이진 탐색으로 접근
import sys

K, N = map(int, sys.stdin.readline().split())
lans = list(map(int, sys.stdin.readlines()))

l, r = 1, max(lans)
while l <= r:
    mid = (l + r) // 2
    cnt = 0
    for lan in lans:
        cnt += lan // mid
    if cnt >= N:
        l = mid + 1
    else:
        r = mid - 1
print(r)