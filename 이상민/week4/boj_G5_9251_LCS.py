a = input()
sa = len(a)
b = input()
sb = len(b)

D = [0]*sb

for ia in range(sa):
    for ib in range(sb-1,-1,-1):
        if a[ia]==b[ib]:
            r=0
            for jb in range(ib):
                if D[jb]>r:r=D[jb]
            if r+1>D[ib]:D[ib]=r+1

print(max(D))