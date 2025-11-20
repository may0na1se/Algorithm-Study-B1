N = int(input())
B = sorted(map(int,input().split()))

S = s = 0
E = e = N-1
R = int(21e8)

while s<e:
    d = B[s]+B[e]
    r = abs(d)
    if r<R: R,S,E=r,s,e
    if d < 0:
        s += 1
    else:
        e -= 1

print(B[S],B[E])