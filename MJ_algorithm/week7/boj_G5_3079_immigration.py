import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

T = [int(input()) for _ in range(N)]

left = 1
right = max(T) * M  #최악의 케이스

while left <= right :
    mid = (left + right) // 2

    pass_count = 0    
    for sec in T:
        pass_count += mid // sec
    
    if pass_count >= M : 
        right = mid-1
    else:
        left = mid + 1
    
print(left)