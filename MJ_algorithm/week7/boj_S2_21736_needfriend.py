import sys
from collections import deque


input =sys.stdin.readline


R, C = map(int, input().split())

campus = [list(input().strip()) for _ in range(R)]

# print(campus)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

visited = [[0]*C for _ in range(R)]

for i in range(R):
  for j in range(C):
    if campus[i][j] == 'I' : #도연이위치찾기
      q = deque([(i,j)]) #바로 bfs시작해주자
      visited[i][j] = 1
      break
  

person_count = 0
while q:
  r,c = q.popleft()
  if campus[r][c] == 'P':
    person_count += 1
    
  for k in range(4):
    next_r, next_c = r + dr[k], c + dc[k]
    
    if next_r < 0 or next_r >= R or next_c < 0 or next_c >= C :
      continue
    
    if visited[next_r][next_c] == 1 :  #이미 간 곳은 안가기
      continue
    
    if campus[next_r][next_c] == 'X' :  #벽이면 추가 안하기
      continue
    
    q.append((next_r, next_c))
    visited[next_r][next_c] = 1
  
  
# print(visited)
if person_count == 0 : 
  print('TT')
else:
  print(person_count)
  