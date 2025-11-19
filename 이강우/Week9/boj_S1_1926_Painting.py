'''
문제: https://www.acmicpc.net/problem/1926
접근:

시간복잡도:
'''

import sys
from collections import deque

# 입력 받기
n, m = map(int, input().split())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)] # 방문 여부 체크 (True/False)

# 방향 벡터
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(x, y):
    dq = deque([(x, y)])
    visited[x][y] = True # 시작점 방문 처리
    area = 1 # 현재 그림의 넓이 (시작점 포함하므로 1부터 시작)
    
    while dq:
        cur_x, cur_y = dq.popleft()
        
        for dx, dy in delta:
            nx, ny = cur_x + dx, cur_y + dy
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if array[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                area += 1 # 넓이 증가
                dq.append((nx, ny))
    return area

num_of_paints = 0
max_area = 0

# 1. 전체 맵을 스캔한다.
for i in range(n):
    for j in range(m):
        # 2. 그림(1)이면서 아직 방문하지 않은 곳을 찾으면 새로운 그림이다.
        if array[i][j] == 1 and not visited[i][j]:
            num_of_paints += 1 # 그림 개수 증가
            current_paint_area = bfs(i, j) # BFS로 이 그림의 넓이 계산
            max_area = max(max_area, current_paint_area) # 최대 넓이 갱신

print(num_of_paints)
print(max_area)