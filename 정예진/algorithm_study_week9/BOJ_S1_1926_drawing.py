# 접근방법 : bfs 여러번 돌리기 ! 지난주 양 문제와 거의 동일합니다
# 풀이 시간 : 30분
import sys
from collections import deque

input = sys.stdin.readlines()
N, M = map(int, input[0].split())
paintings = [list(map(int, input[i].split())) for i in range(1, N+1)]
visited = [[0]*M for _ in range(N)]
drawing_cnt, biggest_paint_size = 0, 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def bfs(x, y):
    global drawing_cnt, biggest_paint_size
    q = deque([(x,y)])
    visited[x][y] = 1

    # 그림 사이즈 초기화
    p_size = 1
    if paintings[x][y] == 1:
        drawing_cnt += 1
    else:
        return

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if paintings[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    p_size += 1
                    q.append((nx,ny))
    if p_size >= biggest_paint_size:
        biggest_paint_size = p_size

for x in range(N):
    for y in range(M):
        if paintings[x][y] == 1 and not visited[x][y]:
            bfs(x,y)

if drawing_cnt == 0:
    biggest_paint_size = 0
print(drawing_cnt)
print(biggest_paint_size)