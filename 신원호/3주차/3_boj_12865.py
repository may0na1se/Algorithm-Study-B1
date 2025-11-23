# dp
# backpack[i]: 배낭에 i만큼 무게를 채웠을 때 가질 수 있는 최대 가치
# backpack의 최대 무게 K에서 물건의 무게 W 까지 dp를 갱신

import sys
N, K = map(int, input().split())
backpack = [0] * (K + 1)
for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    for i in range(K, W - 1, -1):
        backpack[i] = max(backpack[i], backpack[i - W] + V)
print(backpack[K])