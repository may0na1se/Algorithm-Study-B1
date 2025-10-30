N,K,*R = map(int,open(0).read().split())
s = sum(R[:K])
r = s
for i in range(1,N-K+1):
    r += -R[i-1]+R[K+i-1]
    if r>s: s=r
print(s)