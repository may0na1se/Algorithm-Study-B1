n = int(input())
for i in range(1,n):
    x = i + sum(int(a) for a in str(i))
    if x==n:
        print(i)
        break
else: print(0)