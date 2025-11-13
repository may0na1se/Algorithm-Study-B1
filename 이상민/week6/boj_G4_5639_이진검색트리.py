import sys
sys.setrecursionlimit(10**4+1)

def a(e):
    n=S
    while True:
        if e>n:
            if right[n]:
                n=right[n]
            else:
                right[n]=e
                return
        else:
            n=left[n]

def b(n):
    if left[n]: b(left[n])
    if right[n]: b(right[n])
    print(n)

B = [int(b.rstrip()) for b in sys.stdin]
left = [0]*1000000
right = [0]*1000000
S = B[0]

for i in range(1,len(B)):
    if B[i]<B[i-1]: left[B[i-1]]=B[i]
    else: a(B[i])

b(S)
