import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

R, C = map(int, input().split())

board = [[x for x in input().strip()] for _ in range(R)]

# print(board)    

dr = [-1,0,1,0]
dc = [0,1,0,-1]

visited = [[0 for _ in range(C)] for __ in range(R)]
# print(visited)

total_sheep, total_wolf = 0, 0 

for i in range(R):
    for j in range(C):
        if board[i][j] == '#' or visited[i][j] == 1 :
            continue
        local_sheep, local_wolf = 0 , 0
        
        q = deque([(i,j)])

        visited[i][j] = 1
        
        while q:
            r, c = q.popleft()



            # print(r,c)
            
            for _ in range(4):
                next_r , next_c = r + dr[_] , c + dc[_]
                if next_r  < 0 or next_r  >= R or next_c  < 0 or next_c >= C :  #격자 범위 밖으로 나가는지 확인
                    continue

                if board[next_r][next_c] == '#' : #위에서 같이 확인할 수도 있겠지만, 직관성을 위해 작업 분리 
                    continue
                
                if visited[next_r][next_c] == 1 :
                    continue
                
                # print(r,c,next_r,next_c)

                q.append((next_r, next_c))  #상하좌우 칸 중 다음에 갈 수 있는 곳 큐에 추가
                visited[next_r][next_c] = 1
            #이제 지금 현재 칸 검사
            if board[r][c] == 'o' :
                local_sheep += 1
            elif board[r][c] == 'v' :
                local_wolf += 1


        
        if local_sheep > local_wolf :
            total_sheep += local_sheep   #양이 많으면 양이 이김
        else:
            total_wolf += local_wolf  #그외엔 늑대 숫자를 전체카운트에 추가
        
        
print(total_sheep, total_wolf)