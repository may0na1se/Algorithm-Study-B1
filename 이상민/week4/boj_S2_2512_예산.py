N = int(input())
B = [*map(int,input().split())]
M = int(input())

def a(n):
    res = 0
    for b in B:
        res+=min(n,b)
    return res

s,e=0,max(B)
while s<=e:
    m=(s+e)//2
    r=a(m)
    if r<M+1:
        s=m+1
    else:
        e=m-1
print(e)