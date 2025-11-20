import sys
from collections import deque


input = sys.stdin.readline

N = int(input())

li = list(map(int, input().split()))


left = 0
right = len(li)-1
ans = (left, right)
min_sum = li[left] + li[right]

if min_sum == 0 :
  ans = (left,right)
  
else:
  while left < right :
    new_sum = li[left] + li[right]
    if new_sum == 0 :
      ans = (left,right)
      break
    
    if abs(new_sum) < abs(min_sum) :
      min_sum = new_sum
      ans = (left, right)
    
    if new_sum < 0 :
      left += 1
    else:
      right -= 1

print(li[ans[0]], li[ans[1]])