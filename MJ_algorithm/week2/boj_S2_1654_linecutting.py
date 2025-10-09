import sys
# sys.stdin = open('1003/input.txt', 'r')


K, N = map(int, input().split())

lines = [int(input()) for _ in range(K)]

# print(lines)


left = 1
right = max(lines)

while left <= right :

    length = (left + right) // 2
    line_count = 0

    for line in lines:
        line_count += int(line / length) #소수부분 버림

    # print(line_count)

    # if line_count == N :
    #     break

    if line_count < N :  #선 갯수가 모자라다 = 선하나의 길이를 더 줄여서 더 많은 선이 만들어지게
        right = length - 1
    
    if line_count >= N :
        left = length + 1


print(right)

