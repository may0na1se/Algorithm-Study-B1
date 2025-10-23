'''
문제: https://www.acmicpc.net/problem/1932
접근: DP 문제인가 싶음. n이 500까지 가기 때문에, brute-force는 안 됨
그냥 간단하게 내 위치에서 두개씩 대각선 이동하면서 더해주면 됨
n이 500까지니까 대강 500 * 500 * 2번 정도 연산 약 50만번?

시간복잡도: O(N**2 * 2) 인데 너무 큰 거 아닌가 싶긴 하네..
'''

import sys

n = int(input())

triangle = []

for i in range(n):
    nums = tuple(map(int, sys.stdin.readline().split()))
    triangle.append(nums)


results = [[0] * i for i in range(1, n + 1)]
results[0][0] = triangle[0][0]

for i in range(n-1):
    for j in range(len(results[i])):
        for m in range(2):
            results[i + 1][j] = max(results[i][j] + triangle[i + 1][j], results[i + 1][j])
            results[i + 1][j + 1] = max(results[i][j] + triangle[i + 1][j + 1], results[i + 1][j + 1])

# print(results)
print(max(results[-1]))