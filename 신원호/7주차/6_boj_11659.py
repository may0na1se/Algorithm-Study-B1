# boj 11659 구간 합 구하기 4
# 누적합을 이용하면 간단한 문제


import sys
N, M = map(int, sys.stdin.readline().split())
nums = [0] + list(map(int, sys.stdin.readline().split()))
for n in range(1, N + 1):
    nums[n] += nums[n-1]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(nums[j] - nums[i - 1])