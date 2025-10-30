# boj 2636 치즈
# bfs + 구현 문제

import sys
from collections import deque

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 외부의 공기와 치즈 내부의 공기를 구분
def air():
    q = deque([(0, 0)])
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    while q:
        y, x = q.popleft()
        cheese[y][x] = -1
        for dy, dx in delta:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                if cheese[ny][nx] <= 0:
                    visited[ny][nx] = True
                    q.append((ny, nx))


N, M = map(int, input().split())
cheese = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
melted = 0
time = 0

while True:
    air()
    melting = []
    for y in range(N):
        for x in range(M):
            if cheese[y][x] == 1:
                for d in delta:
                    ny, nx = y + d[0], x + d[1]
                    if 0 <= ny < N and 0 <= nx < M and cheese[ny][nx] == -1:
                        melting.append((y, x))
                        break
    if not melting:
        print(time)
        print(melted)
        break
    melted = 0
    for y, x in melting:
        cheese[y][x] = -1
        melted += 1
    time += 1