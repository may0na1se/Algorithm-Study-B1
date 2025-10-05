'''
문제: https://www.acmicpc.net/problem/1912
접근: dp로 접근, 계속 dp문제는 못 풀어서 gemini한테 물어보는 중...

시간복잡도: O(N)
'''

import sys

n = int(input())

lst = [*map(int, sys.stdin.readline().split())]

max_add = -21e8
temp = 0

for i in range(n):
    temp += lst[i]
    max_add = max(max_add, temp)
    if temp < 0:
        temp = 0
    
print(max_add)