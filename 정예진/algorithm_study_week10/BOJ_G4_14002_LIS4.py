# 다 못 품 이렇게 하면 뭔가 될 거 같은데

import sys

input = sys.stdin.readlines()

N = int(input[0])

ls = list(map(int, input[1].split()))

dp = [1] * N
arr = [-1] * N
for i in range(N):
    for j in range(i):
        if ls[j] < ls[i]:
            dp[i] = max(dp[i], dp[j]+1)
            arr[i] = max(arr[i], j)
    print(dp)
    print(arr)
# for idx in range()

print(max(dp))
print(arr)

