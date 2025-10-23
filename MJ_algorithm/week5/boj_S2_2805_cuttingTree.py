import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N, M = map(int, input().split())

trees = list(map(int, input().split()))

# print(trees)


left = 0
right = max(trees)


while left <= right :

    mid = (left + right) // 2

    namu = 0

    for tree in trees:
        if tree - mid > 0 :
            namu += tree - mid
    # print(namu)

    if namu < M :
        right = mid - 1

    else:
        left = mid + 1
    # print(mid, left, right)

print(right)