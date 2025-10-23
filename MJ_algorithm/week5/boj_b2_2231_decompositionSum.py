import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())

left = 1
right = N-1



# p = N
# for num in str(N):
#     p += int(num)

# print(N, p)

while left <= right:
    mid = (left + right) // 2 
    p = mid

    for num in str(mid):
        p += int(num)
    
    if p < N :
        left = mid + 1
    else:
        right = mid - 1

    print(left, right, mid)

