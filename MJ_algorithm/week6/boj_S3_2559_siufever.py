import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temperatures = list(map(int, input().split()))

current_sum = sum(temperatures[0:K])

max_sum = current_sum

#K = 3이라면
#첫 sum = 0, 1, 2
#그다음 sum = 첫 sum - 0번째 + 3번째
#i = 3부터 i-K번째가 빠지고 i번째가 들어오기, N까지

for i in range(K, N):
    #길이가 3이라면 i-3이 빠져나가고 i가 들어오고
    current_sum = current_sum - temperatures[i-K] + temperatures[i]  
    
    max_sum = max(max_sum, current_sum)

print(max_sum)