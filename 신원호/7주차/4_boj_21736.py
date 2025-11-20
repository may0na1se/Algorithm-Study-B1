# boj 21736 헌내기는 친구가 필요해
# bfs

from collections import deque

import sys
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def find():
    for y in range(N):
        for x in range(M):
            if campus[y][x] == 'I':
                return tuple([y, x])

N, M = map(int, input().split())
campus = [list(sys.stdin.readline()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
route = deque([find()])
result = 0
while route:
    ny, nx = route.popleft()
    for d in delta:
        dy, dx = ny + d[0], nx + d[1]
        if 0 <= dy < N and 0 <= dx < M and not visited[dy][dx]:
            visited[dy][dx] = 1
            if campus[dy][dx] == 'X':
                continue
            if campus[dy][dx] == 'P':
                result += 1
            route.append((dy, dx))
if result == 0:
    result = 'TT'
print(result)