from collections import deque

DR = [1,-1,0,0]
DC = [0,0,1,-1]

N,M = map(int,input().split())
B = [[*input()] for _ in range(N)]
for r in range(N):
    for c in range(M):
        if B[r][c] == 'I':
            Q = deque([(r,c)])
            B[r][c] = 'X'

res = 0

while Q:
    r,c = Q.popleft()
    for i in range(4):
        dr,dc = r+DR[i],c+DC[i]
        if dr<0 or dr>=N or dc<0 or dc>=M or B[dr][dc] == 'X': continue
        if B[dr][dc] =='P': res += 1
        B[dr][dc] = 'X'
        Q.append((dr,dc))

print(res if res else 'TT')

Q = deque([()])