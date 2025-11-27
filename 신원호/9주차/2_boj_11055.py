# boj 11055 가장 큰 증가하는 부분 수열
# 수열의 길이가 아닌 수열을 이루는 원소의 합을 비교한다.
# dp에 저장하는 값의 종류만 바뀐 문제


N = int(input())
A = list(map(int, input().split()))

result = A[:]
for i in range(N):
    num = A[i]
    for j in range(i):
        if num > A[j]:
            result[i] = max(result[i], result[j] + num)

print(max(result))