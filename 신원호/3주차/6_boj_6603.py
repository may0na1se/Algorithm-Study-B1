import sys

# 재귀
def lotto(s=[], n=0, k=0):
    if n == 6:
        print(*s)
        return
    for i in range(k, K):
        s.append(S[i])
        lotto(s, n + 1, i + 1)
        s.pop()

while True:
    K, *S = map(int, sys.stdin.readline().split())
    if K == 0:
        break
    lotto()
    print()