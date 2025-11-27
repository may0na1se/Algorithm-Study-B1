# boj 11722 가장 긴 감소하는 부분 수열
# LIS -> LDS
# dp를 구성할 때 원소 간의 비교방식만 달라졌다.

N = int(input())
A = list(map(int, input().split()))
result = [1] * N
for i in range(1, N):
    for j in range(i):
        if A[i] < A[j]:
            result[i] = max(result[i], result[j] + 1)
print(max(result))