'''
문제: https://www.acmicpc.net/problem/2470
접근:

시간복잡도:
'''

N = int(input())
solutions = list(map(int, input().split()))

zero_and_positive = []
negative = []
for n in solutions:
    if n < 0:
        negative.append(n)
    else:
        zero_and_positive.append(n)

negative.sort(reverse=True)
zero_and_positive.sort()

min_comb = list()

