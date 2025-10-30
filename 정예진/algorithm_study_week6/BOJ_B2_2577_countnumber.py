# 접근법 : 형변환으로 0~9가 나오면 더하기
# 풀이 시간 : 3분

import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

val = A * B * C
num_ls = [0] * 10
for num in str(val):
  num_ls[int(num)] += 1

for num in num_ls:
  print(num)