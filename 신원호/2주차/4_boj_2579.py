# dp

import sys

N = int(input())
# 각 인덱스에서의 스테이터스
# stair[i][0]: i-1 번째 계단에서 올라왔을 때의 점수
# stair[i][1]: i-2 번째 계단에서 올라왔을 때의 점수
stair = [[0, 0] for _ in range(N + 1)]
score = int(input())
stair[1][0] = score
if N >= 2:
    # 2번 계단까지는 2번 연속 1칸 오르기가 가능하므로 따로 계산
    score = int(input())
    stair[2][0] = stair[1][0] + score
    stair[2][1] = score
for i in range(3, N + 1):
    score = int(sys.stdin.readline())
    # 이미 1칸 오르기를 했을 경우 2칸 오르기만 가능
    # 2칸 오르기는 언제든 가능
    stair[i][0] = stair[i - 1][1] + score
    stair[i][1] = max(stair[i - 2]) + score
print(max(stair[N]))