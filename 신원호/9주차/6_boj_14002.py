# boj 14002 가장 긴 증가하는 부분 수열 4
# LIS를 복원하는 문제
# N의 범위가 10**3이므로 dp를 이용한 방식과 이분 탐색을 이용하는 방식 모두 가능하다.
# dp를 이용한 풀이

N = int(input())
arr = list(map(int,input().split()))
result = [1] * N
for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            result[i] = max(result[i], result[j] + 1)
print(max(result))
lis = []
cnt = max(result)
idx = N - 1
while cnt > 0 and idx >= 0:
    if result[idx] == cnt:
        lis.append(arr[idx])
        cnt -= 1
    idx -= 1
print(*(lis[::-1]))