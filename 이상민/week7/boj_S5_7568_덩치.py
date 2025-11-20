_,*N = map(int,open(0).read().split())

N = list(zip(N[::2],N[1::2]))
R = []
for i in range(len(N)):
    n = N[i]
    k = 1
    for m in N[:i]+N[i+1:]:
        if m[0] > n[0] and m[1] > n[1]: k+=1
    R.append(k)
print(*R)