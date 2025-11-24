'''
문제: https://www.acmicpc.net/problem/12738
접근: 가장 긴 증가하는 부분 수열2와 같은 원리

시간복잡도: O(NlogN)
'''

N = int(input())
A = list(map(int, input().split()))

dp = [A[0]]

for num in A[1:]:
    if num > dp[-1]:
        dp.append(num)

    else:
        start = 0
        end = len(dp) - 1

        idx = 0
        
        while start <= end:
            mid = (start + end) // 2

            if num > dp[mid]:
                start = mid + 1

            else:
                idx = mid
                end = mid - 1

        dp[idx] = num

# print(dp)
print(len(dp))