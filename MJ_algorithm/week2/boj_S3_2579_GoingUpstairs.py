import sys
# input = sys.stdin.readline
sys.stdin = open('1003/input.txt', 'r')

n = int(input())

stairs = [0] * (n) 
for i in range(n):
    stairs[i] = int(input())

dp = [0] * (n)


if n == 1:
    print(stairs[0])
elif n == 2:
    print(stairs[0] + stairs[1])

else:

    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for i in range(3, n):
        #i-2번째 계단을 밟고 두 칸 오르기
        #i-3 -> i-1을 밟고 한 칸 오르기
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

    print(dp[n-1])
