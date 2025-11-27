import sys

input = sys.stdin.readlines()

N = int(input[0])

ls = list(map(int, input[1].split()))

dp = [1] * N
for i in range(N):
    for j in range(i):
        if ls[j] < ls[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))