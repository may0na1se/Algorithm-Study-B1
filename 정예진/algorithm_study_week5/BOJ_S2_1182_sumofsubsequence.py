# 접근 방법 : 비트마스크로 부분수열 구해서 그 합이 주어진 S면 cnt +1
# 주어진 인풋 해결을 위해서는 주어진 S가 0일 때 공집합을 더하는 경우를 제외해야 정답이 나옴!
# 풀이시간 : 20분
import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in range(1 << N):
    subset = []
    for j in range(N):
        if i & (1 << j):
            subset.append((arr[j]))
    if sum(subset) == S:
        cnt += 1
if S == 0:
    cnt -= 1

print(cnt)