import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
direct = [(-1,0),(1,0),(0,-1),(0,1)]

count = 0
last_cheese = 0

# BFS로 접근
# -> 0,0은 무조건 외부니까 BFS로 외부 공기인지 아닌지 판단
# 만약 arr[nx][ny] = 0이면 외부 공기, q에 추가
# arr[nx][ny] = 1이면 외부공기와 맞닿은 치즈, melt에 추가, 나중에 0으로 바꿔주기
# BFS 끝나고 melt가 없으면 더이상 녹일 치즈가 없다는거니까 count랑 이전 턴에서 녹인 치즈 개수 print
# melt가 있으면 해당 좌표 0으로 바꿔주고 last_cheese에 녹인 치즈 개수 저장, count += 1

while True:
    visited = [[0]*N for _ in range(M)]
    q = deque([(0,0)])
    visited[0][0] = 1
    melt = []

    while q:
        x, y = q.popleft()
        for dx, dy in direct:
            nx, ny = x+dx, y+dy
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = 1
                if arr[nx][ny] == 0:
                    q.append((nx, ny))
                elif arr[nx][ny] == 1:
                    melt.append((nx, ny))

    if not melt:
        print(count)
        print(last_cheese)
        break

    last_cheese = len(melt)
    for x, y in melt:
        arr[x][y] = 0
    count += 1