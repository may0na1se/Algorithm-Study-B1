# boj 2512 예산
# 이분 탐색
# 특정 예산의 배정이 가능한지 판정 후, 이분 탐색으로 가능한 예산의 범위를 좁혀나간다.

import sys

N = int(input())
budgets = list(map(int, sys.stdin.readline().split()))
total = int(input())
if total >= sum(budgets):
    print(max(budgets))
else:
    lower = total // N
    upper = max(budgets)
    while lower <= upper:
        mid = (lower + upper) // 2
        temp_total = 0
        for budget in budgets:
            if budget >= mid:
                temp_total += mid
            else:
                temp_total += budget
        if temp_total <= total:
            lower = mid + 1
        else:
            upper = mid - 1
    print(upper)