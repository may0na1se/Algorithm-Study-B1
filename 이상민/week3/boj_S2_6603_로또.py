def a(n,idx):
    if n==6:
        print(*V)
        return
    for i in range(idx,S):
        V[n]=B[i]
        a(n+1,i+1)
        V[n]=0
while True:
    S,*B = map(int,input().split())
    V = [0]*6
    if S or B:
        a(0,0)
        print()
    else: break