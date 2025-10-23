n = int(input())
N = []
for i in range(1,n):
    x = i + sum(int(a) for a in str(i))
    if x==n: N.append(i)

if N: print(min(N))
else: print(0)