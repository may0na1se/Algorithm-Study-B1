import sys

input =sys.stdin.readline

N, M = map(int, input().split())

li = list(map(int, input().split()))
# print(li)

#최악의 경우 - N , M이 10만이면 
#10만 개 리스트의 조회를 10만 번 해야 하니까..

sum_list = [0]
for x in li:
  sum_list.append(x + sum_list[-1])
  
# print(sum_list)

for _ in range(M):
  s, e  = map(int, input().split())
  print(sum_list[e]-sum_list[s-1])
