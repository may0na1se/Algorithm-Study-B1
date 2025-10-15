# boj 9251 LCS
# dp
# 근데 이거 파이썬 기준 2초면 그냥 완전탐색 돌려도 되는거 아닌가?

s1 = input()
s2 = input()
lcs = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
# lcs[i][j]: s1[:i], s2[:j] 사이의 lcs
for y in range(1, len(s1) + 1):
    for x in range(1, len(s2) + 1):
        if s1[y - 1] == s2[x - 1]:
            lcs[y][x] = lcs[y - 1][x - 1] + 1
        else:
            lcs[y][x] = max(lcs[y - 1][x], lcs[y][x - 1])
print(lcs[-1][-1])