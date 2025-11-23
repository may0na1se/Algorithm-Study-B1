'''
문제: https://www.acmicpc.net/problem/11053
접근: dp 문제, 이중 for문을 사용해서, 입력받은 i번째 수보다 j번째 수가 더 작으면,
그 수의 dp 길이를 찾아, +1한 값보다 dp[i]의 값이 더 작다면, 바꿔주기

시간복잡도: O(N**2)
'''

N = int(input())
A = list(map(int, input().split()))

# 최소길이는 요소 하나의 길이와 동일
dp = [1] * N


for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 이거 잡을 수 있는 TC가 없었나봄
print(dp[-1])