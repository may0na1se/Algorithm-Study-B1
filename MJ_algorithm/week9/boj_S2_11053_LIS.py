import sys

sys.stdin = open('input.txt', 'r')

N = int(input())

nums = list(map(int, input().split()))

# print(nums)


LIS = []


for i in range(N):
  if len(LIS) == 0 or nums[i] > LIS[-1] :
    LIS.append(nums[i])

  elif nums[i] <= LIS[-1] :
    #이때 이진탐색하기
    if len(LIS) > 1 :
      left = 0
      right = len(LIS)-1
      
      while left <= right :
        mid = (left + right) // 2
        if nums[i] <= LIS[mid]:
           right = mid - 1
        else:
          left = mid + 1
          
      # print(LIS)
      LIS[left] = nums[i]

  
  
    elif len(LIS) == 1 :
      LIS[0] = nums[i]
      
print(len(LIS))