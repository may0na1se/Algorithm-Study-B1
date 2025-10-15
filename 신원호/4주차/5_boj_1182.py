# boj 1182 부분수열의 합
# 백트래킹
# O(2^N)

def subsetsum(n, s):
    global count
    if n == N:
        if s == S:
            count += 1
        return
    subsetsum(n + 1, s + nums[n])
    subsetsum(n + 1, s)
    return

N, S = map(int, input().split())
nums = list(map(int, input().split()))
count = 0
subsetsum(0, 0)
if S == 0:
    count -= 1
print(count)