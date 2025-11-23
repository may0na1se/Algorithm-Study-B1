# boj 3184 양
# bfs... 구현 위주의 문제
# 울타리 밖에는 동물이 없다는 점에 유의

import sys
from collections import deque

R, C = map(int, input().split())
field = [sys.stdin.readline().strip() for _ in range(R)]
visited = [[False] * C for _ in range(R)]
delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

sheep_idx = []
wolf_count = 0
for y in range(R):
    for x in range(C):
        if field[y][x] == 'o':
            sheep_idx.append((y, x))
        if field[y][x] == 'v':
            wolf_count += 1

result = [0, 0] # sheep, wolf
for i in range(len(sheep_idx)):
    sy, sx = sheep_idx[i]
    if visited[sy][sx]:
        continue
    visited[sy][sx] = True
    sheep, wolf = 0, 0
    q = deque([(sy, sx)])
    while q:
        ny, nx = q.popleft()
        if field[ny][nx] == 'o':
            sheep += 1
        elif field[ny][nx] == 'v':
            wolf += 1
        for d in delta:
            dy, dx = ny + d[0], nx + d[1]
            if field[dy][dx] == '#':
                continue
            if visited[dy][dx]:
                continue
            visited[dy][dx] = True
            q.append((dy, dx))
    wolf_count -= wolf
    if sheep > wolf:
        result[0] += sheep
    else:
        result[1] += wolf

result[1] += wolf_count
print(*result)