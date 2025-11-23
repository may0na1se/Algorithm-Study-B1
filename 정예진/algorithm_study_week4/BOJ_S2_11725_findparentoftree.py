import sys
from collections import deque

N = int(sys.stdin.readline())
parents = [x for x in range(N+1)]
trees = [list() for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int, sys.stdin.readline().split())
    trees[a].append((a,b))
    trees[b].append((b,a))

start = 1
visited = [0 for _ in range(N+1)]

pq = deque()
pq.append((start, start))
while pq:
    p, c = pq.popleft()
    if visited[c]:
        continue
    visited[c] = 1
    parents[c] = p

    for cand in trees[c]:
        if visited[cand[1]]:
            continue
        pq.append(cand)

for idx in range(2, N+1):
    print(parents[idx])