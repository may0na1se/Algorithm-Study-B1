import sys

input =sys.stdin.readline


N = int(input())

result = []
def p(row):
  if len(result) == N:
    print(*result)
    return
  
  for i in range(1, N+1):
    if i in result:
      continue
    result.append(i)
    p(row + 1)
    
    result.pop()
    
p(1)