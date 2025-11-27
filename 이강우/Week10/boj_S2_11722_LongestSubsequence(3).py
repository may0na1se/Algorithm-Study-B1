'''
문제: https://www.acmicpc.net/problem/11722
접근: 가장 긴 증가하는 부분수열과 같은 원리

시간복잡도: O(N**2)
'''

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if A[j] > A[i]:
            dp[i] = max(dp[i], dp[j] + 1)


print(max(dp))