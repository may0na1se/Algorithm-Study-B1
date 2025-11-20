from collections import deque

DR = [1,-1,0,0]
DC = [0,0,1,-1]

def a(r,c):
    Q = deque([(r,c)])
    o = v = 0
    if B[r][c] == 'o': o+=1
    if B[r][c] == 'v': v+=1
    B[r][c] = '#'
    while Q:
        r,c = Q.popleft()
        for i in range(4):
            dr,dc = r+DR[i],c+DC[i]
            if dr<0 or dr>=N or dc<0 or dc>=M or B[dr][dc] == '#': continue
            if B[dr][dc] == 'o': o += 1
            if B[dr][dc] == 'v': v += 1
            B[dr][dc] = '#'
            Q.append((dr,dc))
    if o>v: v=0
    else: o=0
    return o,v

N,M = map(int,input().split())
B = [[*input()]for _ in range(N)]
O = V = 0
for r in range(N):
    for c in range(M):
        if B[r][c] == '#': continue
        ro,rv = a(r,c)
        O+=ro
        V+=rv

print(O,V)