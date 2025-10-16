'''
문제: https://www.acmicpc.net/problem/2579
접근: 원호님의 힌트로 DP로 푸는 것이라는 것을 알게 되었다.
그래서 set()을 만들어서 DP로 풀어보았다.
근데 메모리 초과 뜸

시간복잡도: 
'''

   

S = int(input())
scores = [int(input()) for _ in range(S)]

if S == 1:
    print(scores[0])

elif S == 2:
    print(scores[0] + scores[1])

else:
    # 1칸 전에서 온게 index 0, 2칸 전에서 온 게 index 1
    dp = [[0, 0] for _ in range(S)]

    # 첫번째 계단
    dp[0][0] = scores[0]
    # 두번째 계단
    dp[1][0] = scores[1] + dp[0][0]
    dp[1][1] = scores[1] # 2칸 전이 없으니

    for i in range(2, S):
        dp[i][0] = scores[i] + dp[i-1][1] # 1칸 전에서 왔다. -> 연속 3칸은 불가
        dp[i][1] = scores[i] + max(dp[i-2]) # 2칸 전에서 왔다.

    # print(scores)
    # print(dp)
    print(max(dp[-1]))