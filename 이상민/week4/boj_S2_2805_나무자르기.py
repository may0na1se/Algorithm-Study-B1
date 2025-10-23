def a(n):
    res = 0
    for b in B:
        if b>n:res+=b-n
    return res

N,M = map(int,input().split())
B = [*map(int,input().split())]

s,e=0,max(B)

while s<=e:
    m=(s+e)//2
    if a(m)<M:
        e=m-1
    else:
        s=m+1

print(e)
