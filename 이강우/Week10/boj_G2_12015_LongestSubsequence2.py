'''
문제: https://www.acmicpc.net/problem/12015
접근:

시간복잡도:
'''

'''
예시 입력
4
10 20 30 15

6
10 20 30 15 18 19
'''

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# 가장 긴 부분 수열의 길이를 계산하기 위한 dp
dp = [A[0]]

for num in A[1:]:
    if num > dp[-1]:
        dp.append(num)

    # 가장 긴 부분수열의 길이는 유지하되,
    # 추후 오는 수를 받기 위한 가장 유리한 부분수열(dp)을 만들어줌
    # 수의 순서는 이상할 수 있으나, 길이는 유지됨
    else:
        start = 0
        end = len(dp) - 1

        idx = 0
        
        # start < end인지, start <= end인지 헷갈림..
        while start <= end:
            mid = (start + end) // 2

            if num > dp[mid]:
                start = mid + 1

            else:
                idx = mid
                end = mid - 1

        # 수의 순서는 무너질 수 있어도, 길이는 유지됨
        dp[idx] = num


# print(dp)
print(len(dp))