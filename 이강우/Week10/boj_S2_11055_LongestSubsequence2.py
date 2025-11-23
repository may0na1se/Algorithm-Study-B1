'''
문제: https://www.acmicpc.net/problem/11055
접근: 가장 긴 부분수열의 길이를 구하는 것과 같은 원리.
다만, 길이처럼 1씩 증가가 아닌, 요소의 크기만큼 증가하기 때문에,
마지막에는 dp[-1]이 아닌 max(dp)가 필요

시간복잡도: O(N**2) + O(N) 이중for문 + max값 찾기
'''

N = int(input())
A = list(map(int, input().split()))

# 합을 기록해줄 dp 생성
dp = [0] * N

for i in range(N):
    dp[i] = A[i]
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + A[i])

print(max(dp))