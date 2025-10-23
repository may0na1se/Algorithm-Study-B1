'''
문제: https://www.acmicpc.net/problem/9251
접근: LCS 알고리즘이라고 한다... 구글에서 LCS 개념 배워서 그냥 풀었음

시간복잡도: O(N * M)
'''


str1 = input()
str2 = input()

# 행 열 계산 반대로 해서 index error 났음
arr = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            arr[i][j] = arr[i - 1][j - 1] + 1
        else:
            arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])

print(arr[-1][-1])