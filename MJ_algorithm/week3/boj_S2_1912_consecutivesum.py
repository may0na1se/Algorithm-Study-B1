import sys
# input = sys.stdin.readline

sys.stdin = open('input.txt', 'r')

n = int(input())
arr = list(map(int, input().split()))

# print(arr)

dp = [0] * n


# print(dp)
if n == 1 :
    print(arr[0])
else:
    dp[0] = arr[0]
    dp[1] = max(arr[1], dp[0]+arr[1])
    for i in range(2, n):
        dp[i] = max(arr[i], dp[i-1] + arr[i])

    # print(dp)


    print(max(dp))