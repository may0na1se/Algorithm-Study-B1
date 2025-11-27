# boj 12015 가장 긴 증가하는 부분 수열 2
# N의 최댓값이 10**6으로 늘어났기 때문에 시간복잡도 O(N^2)으로는 어렵다.
# 이분 탐색을 이용하는 방식, 시간복잡도 O(NlogN)

def binary_search(lower, upper, num):
    while lower < upper:
        mid = (lower + upper) // 2
        if lis[mid] < num:
            lower = mid + 1
        else:
            upper = mid
    return upper


N = int(input())
A = list(map(int, input().split()))
lis = [A[0]]

for i in range(1, N):
    if lis[-1] < A[i]:
        lis.append(A[i])
    else:
        pos = binary_search(0, len(lis), A[i])
        lis[pos] = A[i]

print(len(lis))