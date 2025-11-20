from collections import deque

DR = [1,-1,0,0]
DC = [0,0,1,-1]

def a(r,c):
    Q = deque([(r,c)])
    B[r][c] = 0
    res = 1
    while Q:
        r,c = Q.popleft()
        for i in range(4):
            dr,dc = r+DR[i],c+DC[i]
            if dr<0 or dr>=N or dc<0 or dc>=M or B[dr][dc] == 0: continue
            res+=1
            B[dr][dc] = 0
            Q.append((dr,dc))
    return  res

N,M = map(int,input().split())
B = [[*map(int,input().split())]for _ in range(N)]
cnt = RES = 0
for r in range(N):
    for c in range(M):
        if B[r][c] == 0: continue
        cnt+=1
        res = a(r,c)
        if res>RES:RES=res

print(cnt)
print(RES)