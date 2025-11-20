'''
문제: https://www.acmicpc.net/problem/6236
접근:

시간복잡도:
'''

import sys
        

N, M = map(int, input().split())

budgets = []
rest = 0

for _ in range(N):
    budgets.append(int(sys.stdin.readline()))

print(budgets)

l = 1
r = max(budgets)

while l < r:
    cnt = 0
    mid = (l + r) // 2

    for bud in budgets:
        if cnt > M:
            break
        if rest < bud:
            if rest + mid < bud:
                cnt = M + 1
                break

            rest = rest + mid - bud
            cnt += 1
        else:
            rest -= bud
    
    if cnt > M:
        l = mid
    else:
        r = mid

print(l, r)