def a1(a):
  print(a,end='')
  if left[a]:a1(left[a])
  if right[a]:a1(right[a])
def a2(a):
  if left[a]:a2(left[a])
  if right[a]:a2(right[a])
  print(a,end='')
def a3(a):
  if left[a]:a3(left[a])
  print(a,end='')
  if right[a]:a3(right[a])


N = int(input())
left = {chr(k):0 for k in range(65,91)}
right = {chr(k):0 for k in range(65,91)}
for _ in range(N):
  k,l,r = input().split()
  if l!='.':left[k]=l
  if r!='.':right[k]=r
a1('A')
print()
a3('A')
print()
a2('A')