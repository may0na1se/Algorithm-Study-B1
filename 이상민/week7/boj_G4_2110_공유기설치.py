def a(w):
    r=1
    n=B[0]
    for b in B[1:]:
        if b-n<w: continue
        r+=1
        n=b
    return r

N,M = map(int,input().split())
B = sorted(int(input())for _ in range(N))

s,e = 0,max(B)-min(B)

while s<=e:
    m = (s+e)//2
    if a(m)<M: e=m-1
    else: s=m+1

print(e)