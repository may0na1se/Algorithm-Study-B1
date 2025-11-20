import sys
from collections import deque


sys.stdin = open('input.txt', 'r', encoding='utf-8-sig')
input = sys.stdin.readline

R, C = map(int, input().split())

paper = [list(map(int, input().split())) for _ in range(R)]

# print(paper)


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


painting_count = 2

max_area = 0

for i in range(R):
  for j in range(C):
    if paper[i][j] != 1 : 
      continue
    
    q = deque([(i,j)])
    paper[i][j] = painting_count
    
    current_area = 1
    
    while q:
    
      r, c = q.popleft()
      
      for k in range(4):
        next_r, next_c = r + dr[k], c + dc[k]
        
        
        
        if next_r < 0 or next_r >= R or next_c < 0 or next_c >= C :
          continue
        
        
        
        if paper[next_r][next_c] != 1 :
          continue
        
        #print(next_r, next_c)
        
        q.append((next_r, next_c))
        current_area += 1 
        paper[next_r][next_c] = painting_count
      

    painting_count += 1
    
    if current_area > max_area :
      max_area = current_area
    
    # print(paper)      

print(painting_count-2)
print(max_area)