def abc(n):
    res=0
    for b in B:
        res+=n//b
    return res

N,M = map(int,input().split())
B = [int(input())for _ in range(N)]

s,e = 0,max(B)*M

while s<=e:
    m = (s+e)//2
    if abc(m)<M: s=m+1
    else: e=m-1

print(s)