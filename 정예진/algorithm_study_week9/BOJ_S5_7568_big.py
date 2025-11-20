# 접근방법 : 그냥 완전탐색!
# 풀이시간 : 20분
import sys

input = sys.stdin.readlines()
N = int(input[0])

people = []
for _ in range(1, N+1):
    w, h = map(int, input[_].strip().split())
    people.append((w,h))

rank = [0]* N

for idx in range(N):
    cnt = 0
    n_weight, n_height = people[idx]
    for i in range(N):
        if idx != i:
            weight, height = people[i]
            if n_weight < weight and n_height < height:
                cnt += 1
    rank[idx] = cnt + 1

print(*rank)