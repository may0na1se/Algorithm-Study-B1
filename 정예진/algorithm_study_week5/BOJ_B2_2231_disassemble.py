# 접근 방법 : 미친듯한 형변환과 함께 편하게 구하기
# string으로 입력 받기 : 자릿수 구하기 -> int로 변환 : for문 range로 활용 -> str로 변환 : 각 자릿수별로 list에 넣기
# -> int로 변환 : 자릿수별 총합 구하기 -> num + 자릿수별 총합이 N이면 break , for문 끝까지 돌아도 없으면 0 출력
# for문 범위 : 각 자리가 모두 9일 때 자릿수별 합산이 최대가 되므로 최솟값을 N - 9 *(자릿수) 로 설정
# 풀이시간 : 30분

import sys

N = sys.stdin.readline().strip()

n = len(N)
N = int(N)
for num in range(max(0, N-9*n), N):   # 여기서 N-9*N 이 음수가 될 수 있음을 간과함 -> max(0, val) 로 음수 안 내려가게 조절
    number = str(num)
    ls = [int(x) for x in number]
    if num + sum(ls) == N:
        print(num)
        break
else:
    print(0)