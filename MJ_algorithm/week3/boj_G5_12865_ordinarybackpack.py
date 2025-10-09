import sys
# input = sys.stdin.readline

sys.stdin = open('input.txt', 'r')


N, K = map(int, input().split())

bag = []
for _ in range(N):
    W, V = map(int, input().split())
    if W <= K :
        bag.append((W,V))

print(bag)

dp = [0] * len(bag)
bag.sort()
print(bag)


dp[0] = bag[0][1]