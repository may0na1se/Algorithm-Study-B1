# boj 12738 가장 긴 증가하는 부분 수열 3
# 수열의 원소의 값의 범위에 음수가 추가된 문제
# 기존의 이분탐색 방식을 사용한다면 해결 방식의 변화는 없다.

import sys

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