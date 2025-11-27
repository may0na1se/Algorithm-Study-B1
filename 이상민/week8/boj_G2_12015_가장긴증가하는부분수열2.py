def aaa(s,e,b):
    while s<=e:
        m = (s+e)//2
        if b > P[m]: s = m+1
        else: e = m-1
    return s

N = int(input())
B = [*map(int,input().split())]
P = [0]*N
P[0] = B[0]
e = 0

for i in range(1,N):
    if B[i] > P[e]:
        e += 1
        P[e] = B[i]
    else:
        P[aaa(0,e,B[i])] = B[i]

print(e+1)