# 접근 방법 : DP! 연속 3개는 못 올라간다라는 걸 어떻게 조건으로 설정할지가 좀 어려웠던 문제

import sys

n = int(sys.stdin.readline())
stair = [int(sys.stdin.readline()) for _ in range(n)]

if n == 1:
    print(stair[0])
elif n == 2:
    print(stair[0] + stair[1])
else:
    dp = [0] * n
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1]
    dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

    for i in range(3, n):
        dp[i] = max(dp[i-2], dp[i-3] + stair[i-1]) + stair[i]

    print(dp[-1])
