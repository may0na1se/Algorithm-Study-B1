# 접근방법 : BFS..
# 풀이 시간 : 30분 (영역 순회를 어떻게 할지 고민을 좀 했습니다)
import sys
from collections import deque
input = sys.stdin.readlines()

R, C = map(int, input[0].split())
yard = [list(input[r].strip()) for r in range(1, R+1)]

visited = [[0]*C for _ in range(R)]
total_sheep, total_wolf = 0, 0

# 상하좌우 이동 방향
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    global total_sheep, total_wolf

    q = deque([(r, c)])
    visited[r][c] = 1

    # 영역 내의 양과 늑대 개수 초기화
    n_sheep = 0
    n_wolf = 0

    if yard[r][c] == 'o': # 양
        n_sheep += 1
    elif yard[r][c] == 'v': # 늑대
        n_wolf += 1

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < R and 0 <= nc < C:
                if yard[nr][nc] != '#' and not visited[nr][nc]:  # '#'는 울타리니까 패스
                    visited[nr][nc] = 1 # 영역 순회하면서 방문 처리하기
                    q.append((nr, nc))

                    if yard[nr][nc] == 'o':
                        n_sheep += 1
                    elif yard[nr][nc] == 'v':
                        n_wolf += 1

    # 양이 더 많으면 양만 생존, 늑대가 더 많으면 늑대만 생존
    if n_sheep > n_wolf:
        total_sheep += n_sheep
    else:
        total_wolf += n_wolf


for r in range(R):
    for c in range(C):
        # 울타리 X + 방문 안한 곳이 시작
        if yard[r][c] != '#' and not visited[r][c]:
            bfs(r, c)

print(total_sheep, total_wolf)