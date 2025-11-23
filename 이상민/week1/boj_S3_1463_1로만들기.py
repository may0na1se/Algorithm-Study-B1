from collections import deque

N = int(input())
V = [0]*(N+1)
Q = deque()
Q.append(N)
while Q:
    n = Q.popleft()
    if n==1:
        print(V[1])
        break
    if not n%3 and not V[n//3]:
        V[n//3] = V[n]+1
        Q.append(n//3)
    if not n%2 and not V[n//2]:
        V[n//2] = V[n]+1
        Q.append(n//2)
    if not V[n-1]:
        V[n-1] = V[n]+1
        Q.append(n-1)