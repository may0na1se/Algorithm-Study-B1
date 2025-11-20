# 접근 방법 : 두 합의 절댓값이 0에 가까운 두 수를 뽑는 문제
# 처음에는 조합 생각, 근데 최대 n 수가 100,000 인거 보고 포기
# 그래서 주어진 수를 정렬하고 양끝에서 범위를 좁혀오면서 탐색하자는 생각
# 두 수의 합의 절댓값이 min_val보다 작으면 min_val과 answer 업데이트
# 그리고 두 수의 합이 0보다 크면 r를 하나 줄이고, 0보다 작으면 l를 하나 올리는 식으로
# 그래서 l,r이 교차하는 순간 종료 (전체 수 순회했으니까)
# 풀이 시간 : 40분

import sys

input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))

l,r = 0, N-1
min_val = float('inf')
ans = (arr[l], arr[r])

while l<r:
    s = arr[l] + arr[r]
    if min_val > abs(s):
        min_val = abs(s)
        ans = (arr[l], arr[r])

    if s > 0:
        r -= 1
    else:
        l += 1

print(ans[0],ans[1])

