# 접근법 : 간단한 슬라이딩 윈도우 문제
# 처음 K개만큼의 합을 total에 저장해두고 그 이후 리스트를 한번 순회
# 그러면서 기존 배열의 첫번째꺼 빼주고 그다음 인덱스의 값 더해주기
# 풀이 시간 : 5분
import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

total = sum(arr[:K])
max_tot = total

for idx in range(K, N):
    total += arr[idx] - arr[idx-K]
    if max_tot <= total:
        max_tot = total

print(max_tot)