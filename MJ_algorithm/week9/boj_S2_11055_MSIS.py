import sys


sys.stdin = open('input.txt', 'r', encoding='utf-8-sig')

input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

dp = nums[:]

for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+nums[i])

print(max(dp))