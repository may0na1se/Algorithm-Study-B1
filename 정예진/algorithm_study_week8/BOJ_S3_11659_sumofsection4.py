# 접근방법 : 처음에는 그냥 인덱스로 접근하는 방식 썼는데 그럼 엄청나게 많이 돌아버림!!! > 첫시도 시간초과 ㅜㅜ
# 그래서 한번 입력받은 arr을 순회하면서 누적합을 저장하고,
# i,j 받으면 j번째까지의 누적합에서 i-1번째까지의 누적합을 빼는 방식
# 첫번째 인덱스 처리를 위해 [0]을 첫번째 요소로 넣어줌 -> 그럼 인덱스 계산이 편해요

import sys
input = sys.stdin.readlines()

N, M = map(int, input[0].split())
arr = [0] + list(map(int, input[1].split()))
for idx in range(1, N+1):
    arr[idx] += arr[idx-1]

for cnt in range(2, M+2):
    i, j = map(int, input[cnt].split())
    print(arr[j] - arr[i-1])
