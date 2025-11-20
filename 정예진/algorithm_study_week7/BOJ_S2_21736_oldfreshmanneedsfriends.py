# 접근 방법 : BFS 구현... 그냥 평범한 BFS
# 소요시간 : 20분? 구현이 그냥 좀 오래 걸린듯
import sys
from collections import deque

input = sys.stdin.readline()

N, M = map(int, input.split())

campus = [list(sys.stdin.readline().strip()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            I_x, I_y = i, j
            break


def bfs(x,y):
    direct = [(-1,0),(1,0),(0,-1),(0,1)]
    visited = [[0]*M for _ in range(N)]
    visited[x][y] = 1
    queue = deque()
    queue.append((x,y))
    cnt = 0
    while queue:
        nx, ny = queue.popleft()
        for dx, dy in direct:
            n_x, n_y = nx+dx, ny+dy
            if 0<=n_x<N and 0<=n_y<M and not visited[n_x][n_y]:
                if campus[n_x][n_y] == "P":
                    cnt +=1
                    visited[n_x][n_y] = 1
                    queue.append((n_x,n_y))
                elif campus[n_x][n_y] == "O":
                    visited[n_x][n_y] = 1
                    queue.append((n_x,n_y))
                elif campus[n_x][n_y] == "X":
                    visited[n_x][n_y] = 1
    if cnt == 0:
        print("TT")
    else:
        print(cnt)


bfs(I_x, I_y)