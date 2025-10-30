import sys
input = sys.stdin.readline

N = int(input())

liquids = list(map(int, input().split()))

liquids.sort()

# print(liquids)

left = 0
right = len(liquids)-1
min_sum = liquids[left]+liquids[right]
ans = (left,right)
#-99 -2 -1 4 98 




if min_sum == 0 : 
  ans = (left, right)
else:
  
  while left < right:
    new_sum = liquids[left] + liquids[right]
    if new_sum == 0:
      ans = (left, right)
      break
    
    if abs(new_sum) < abs(min_sum):
      min_sum = new_sum
      ans = (left, right)
      
    if new_sum < 0 :
      left += 1 
    else:
      right -= 1    
      
    
# print(ans[-1], min_sum)
# print(ans)
print(liquids[ans[0]], liquids[ans[1]])
      
 