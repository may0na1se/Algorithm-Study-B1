'''
문제: https://www.acmicpc.net/problem/2231
접근:

시간복잡도:
'''

N = int(input())
temp = N
cnt = 0

while temp > 0:
    temp //= 10
    cnt += 1

digits = [0] * cnt
digits[0] = 1

idx = 0

while idx < cnt:
    num = 0

    for i in range(cnt):
        num += digits[i] * 10 ** (cnt - 1 - i)

    if num < N:
        digits[idx] += 1
    else:
        pass