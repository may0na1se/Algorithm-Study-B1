def a(n,idx):
    if n==N//2:
        global res
        pp = mm = 0
        for r in range(N):
            for c in range(N):
                if V[r]==V[c]:
                    if V[r]:
                        pp+=B[r][c]
                    else: mm+=B[r][c]
        rr = abs(pp-mm)
        if rr<res:res=rr
        return
    for i in range(idx,N):
        V[i]=1
        a(n+1,i+1)
        V[i]=0
    

N = int(input())
B = [[*map(int,input().split())]for _ in range(N)]
V = [0]*N
res = sum(sum(b) for b in B)
a(0,0)
print(res)