# boj 2467 용액
# 투포인터

import sys

N = int(input())
solutions = list(map(int, sys.stdin.readline().split()))
front, rear = 0, N - 1
a, b = solutions[front], solutions[rear]
now = a + b
result = now
while front + 1 < rear:
    if now > 0:
        rear -= 1
        now = solutions[front] + solutions[rear]
        if abs(now) < abs(result):
            a, b = solutions[front], solutions[rear]
            result = now
    elif now < 0:
        front += 1
        now = solutions[front] + solutions[rear]
        if abs(now) < abs(result):
            a, b = solutions[front], solutions[rear]
            result = now
    else:
        break

print(a, b)