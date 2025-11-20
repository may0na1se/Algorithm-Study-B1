import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

l,r = 0, N-1
min_val = float('inf')
ans = (arr[l], arr[r])

while l<r:
    s = arr[l] + arr[r]
    if min_val > abs(s):
        min_val = abs(s)
        ans = (arr[l], arr[r])

    if s > 0:
        r -= 1
    else:
        l += 1


print(ans[0],ans[1])
