'''
문제: https://www.acmicpc.net/problem/2512
접근: 간단한 이진탐색으로 풀 수 있었다. 코드 구현을 못 했다.

시간복잡도:
'''

N = int(input())

nums = list(map(int, input().split()))

budget = int(input())

lower = budget // N
upper = max(nums)


if sum(nums) <= budget:
  print(max(nums))

else:
  while lower <= upper:
    under, over = 0, 0
    mid = (lower + upper) // 2

    for i in range(N):
      if nums[i] <= mid:
        under += nums[i]
      else:
        over += mid

    if under + over <= budget:
      lower = mid + 1
    elif under + over > budget:
      upper = mid - 1



  print(lower-1)
  # print(upper-1)
  # print(mid)