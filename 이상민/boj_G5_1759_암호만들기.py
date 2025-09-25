Q = set(['a','e','i','o','u'])

def a(n,i,s,p,q):
    if n==L:
        if p>1 and q>0:
            print(s)
        return
    for j in range(i,C):
        if B[j] in Q: a(n+1,j+1,s+B[j],p,q+1)
        else: a(n+1,j+1,s+B[j],p+1,q)

L,C = map(int,input().split())
B = sorted(input().split())
a(0,0,'',0,0)