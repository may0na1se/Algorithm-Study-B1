import sys

input = sys.stdin.readlines()

N = int(input[0])
arr = list(map(int, input[1].split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))