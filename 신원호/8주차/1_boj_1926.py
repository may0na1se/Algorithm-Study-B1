# boj 1926 그림
# bfs를 사용해서 세그먼트의 수와 넓이를 구하자

from collections import deque

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
checked = [[False] * m for _ in range(n)]

delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
result = 0
result_count = 0
for y in range(n):
    for x in range(m):
        if checked[y][x] or not paper[y][x]:
            continue
        picture = 1
        q = deque([(y, x)])
        checked[y][x] = True
        while q:
            ny, nx = q.popleft()
            for d in delta:
                dy, dx = ny + d[0], nx + d[1]
                if not (0 <= dy < n and 0 <= dx < m):
                    continue
                if checked[dy][dx] or not paper[dy][dx]:
                    continue
                q.append((dy, dx))
                checked[dy][dx] = True
                picture += 1
        result = max(result, picture)
        result_count += 1

print(result_count)
print(result)
