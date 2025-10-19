'''
문제: https://www.acmicpc.net/problem/2805
접근: 이진탐색이라고 생각했음 근데 다 틀림

시간복잡도:
'''

N, M = map(int, input().split())

trees = list(map(int, input().split()))
trees.sort()

lower = 1
upper = trees[-1]

while lower < upper:
    mid = (lower + upper) // 2

    earned = 0

    for i in range(N):
        if trees[i] <= mid:
            continue
        earned += trees[i] - mid
    
    if earned > M:
        lower = mid + 1
    elif earned < M:
        upper = mid - 1
    elif earned == M:
        break

if earned == M:
    print(mid)
else:
    print(lower)