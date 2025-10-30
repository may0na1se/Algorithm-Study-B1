# boj 1477 휴게소 세우기
# 이진 탐색

import sys

def divide(length):
    count = 0
    for dist in interval:
        count += (dist - 1) // length
        if count > M:
            return False
    return True


N, M, L = map(int, sys.stdin.readline().split())
rest = list(map(int, sys.stdin.readline().split()))
rest.append(0)
rest.append(L)
rest.sort()
interval = [rest[i + 1] - rest[i] for i in range(N + 1)]
upper = max(interval)
lower = 1
while lower <= upper:
    mid = (lower + upper) // 2
    if divide(mid):
        upper = mid - 1
    else:
        lower = mid + 1

print(lower)