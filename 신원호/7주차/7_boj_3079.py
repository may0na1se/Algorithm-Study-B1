# boj 3079 입국심사
# 처음에 힙큐를 사용했었는데 시간초과
# 이분탐색으로 풀어야 시간내에 가능한듯


import sys

def able(limit):
    total = 0
    for delay in T:
        total += limit // delay
    if total >= M:
        return True
    return False


N, M = map(int, input().split())
T = [int(sys.stdin.readline()) for _ in range(N)]
lower = 0
upper = max(T) * M

while lower <= upper:
    mid = (lower + upper) // 2
    if able(mid):
        upper = mid - 1
    else:
        lower = mid + 1

print(lower)