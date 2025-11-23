def a(n):
    if n == N:
        print(*B)
        return
    for i in range(N):
        if V[i]: continue
        V[i] = 1
        B[n] = i+1
        a(n+1)
        B[n] = 0
        V[i] = 0

N = int(input())
V = [0]*N
B = [0]*N
a(0)