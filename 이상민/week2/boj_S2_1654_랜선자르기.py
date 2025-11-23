def a(s,e):
    if e==1:
        print(1)
        return 
    if s>e:
        print(e)
        return
    m = (s+e)//2
    res = sum(b//m for b in B)
    if res<N: a(s,m-1)
    else: a(m+1,e)

K,N = map(int,input().split())

B = [int(input()) for _ in range(K)]
M = max(B)

a(0,M)