def a(n):
    c = r = 0
    for b in B:
        if c+b>n:
            c=b
            r+=1
        else: c+=b
    return r+1

N,M = map(int,input().split())
B = [int(input())for _ in range(N)]

s,e = max(B),int(21e8)

while s<=e:
    m=(s+e)//2
    if a(m)>M: s=m+1
    else: e=m-1

print(s)