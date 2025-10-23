'''
문제: https://www.acmicpc.net/problem/2805
접근: 이진탐색이라고 생각했음. 코드 잘 기억해서 다시 풀음.
다만, 시간이 너무 많이 걸리는 것 같음

시간복잡도:
'''

N, M = map(int, input().split())

trees = list(map(int, input().split()))

lower = 1
upper = max(trees)

while lower <= upper:
  mid = (lower + upper) // 2

  cut = 0

  for tree in trees:
    if tree > mid:
      cut += tree - mid

  if cut < M:
    upper = mid - 1
  else:
    lower = mid + 1

# print(lower)
print(upper)