A = int(input())
B = int(input())
C = int(input())

N = A*B*C

ans = [0] * 10

for i in range(0,10):
    for _ in str(N):
        if str(i) == _:
            ans[i] += 1

for _ in list(ans):
    print(_)