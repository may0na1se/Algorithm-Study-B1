# 접근 방법 : 이건 그냥 쉬운 DP였던 거 같습니다
# 지금까지의 누적합과 현재의 값 중 더 큰 값을 선택하면서 O(N)으로 문제 풀이 가능!
# 걸린 시간 : 30분?

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [0] * N
dp[0] = arr[0]

for i in range(1, N):
    dp[i] = max(arr[i], dp[i-1]+arr[i])

print(max(dp))