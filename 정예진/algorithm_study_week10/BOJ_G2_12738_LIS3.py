# 접근방법 : for문 돌면서 이분탐색을 한다! -> 강우오빠가 디코에서 얘기해준 거 참고하긴 함
# 이분탐색 : DP list에 어디 들어갈지 - 만약 list 내의 값 중 가장 크면 추가, 어딘가에 들어갈 수 있으면 그 자리 대체
# DP : 이 수열 안에서 증가하기만 하면 됨

import sys

input = sys.stdin.readlines()
N= int(input[0])
arr = list(map(int, input[1].split()))
dp = []

def binary_search(x, dp):
    l, r = 0, len(dp)

    while l<r:
        mid = (l + r) // 2
        if x > dp[mid]:  # 여기서 = 넣어서 틀림 ㅋㅋ
            l = mid + 1
        else:
            r = mid
    return l

for x in arr:
    pos = binary_search(x, dp)
    if pos == len(dp):
        dp.append(x)
    else:
        dp[pos] = x

print(len(dp))

