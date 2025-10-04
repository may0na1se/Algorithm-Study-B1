'''
문제: https://www.acmicpc.net/problem/12865
접근: DP라고 생각은 됨. 근데 못 풀겠어서 젬미니한데 물어봄
이 문제는 DP 중 Knapsack 문제라고 한다.
그냥 dfs 식으로 하면 시간 초과 무조건이고,
각 무게별로 최대한 담을 수 있는 가치를 구해서 저장하고,
그 저장된 값을 더 큰 무게를 구할 때 활용하는 것

시간복잡도: O(N*K)라고 하는구나
'''



N, K = map(int, input().split())

stuffs = [0] * N

for i in range(N):
    W, V = map(int, input().split())
    stuffs[i] = (W, V)

max_value = 0

dp = [0] * (K+1)

for i in range(N):
    weight = stuffs[i][0]
    value = stuffs[i][1]
    for j in range(K, -1, -1):
        if j - weight < 0:
            continue
        dp[j] = max(dp[j], dp[j - weight] + value)

print(dp[K])