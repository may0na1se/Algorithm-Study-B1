'''
문제: https://www.acmicpc.net/problem/1926
접근:

시간복잡도:
'''

import sys
from collections import deque


n, m = map(int, input().split())

array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

if array[0][0]:
    area = 1
else:
    area = 0

dq = deque([(0, 0, area)])

max_area = 0
max_x, max_y = 0, 0

if area:
    num_of_paints = 1
else:
    num_of_paints = 0

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

while dq:
    cur_x, cur_y, cur_area = dq.popleft()

    if cur_area > max_area:
        max_area = cur_area
        max_x, max_y = cur_x, cur_y

    for dx, dy in delta:
        nx, ny = cur_x + dx, cur_y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if visited[nx][ny]:
            continue
        if array[nx][ny] == 0:
            visited[nx][ny] = -1
            dq.append((nx, ny, 0))
            continue
        else:
            # 방문 안 했음, 0이 아닌 경우만 탐색
            cur_area += 1
            if not visited[nx][ny] and cur_area == 1:
                num_of_paints += 1
            if visited[cur_x][cur_y] < cur_area:
                visited[cur_x][cur_y] = cur_area
            dq.append((nx, ny, cur_area))
            

print(num_of_paints)
print(visited[max_x][max_y])