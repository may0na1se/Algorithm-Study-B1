'''
문제: https://www.acmicpc.net/problem/11286
접근: 힙을 들어오는 수의 절댓값을 기준으로 구성하면서, 출력은 들어오는 수로 하기
튜플로 (절댓값, 원래 수) 이렇게 구성해서 절댓값을 기준으로 들어가게 했음.
절댓값이 같을 때에는 자동적으로 원래 수를 기준으로 적용이 됨. 

시간복잡도: 힙이니까 대충 O(NlogN) 정도일 듯
'''

import sys
from heapq import heappop, heappush

N = int(input())

abs_q = []
result = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if not x:
        if not abs_q:
            result.append(0)
        else:
            a = heappop(abs_q)
            result.append(a[1])
    else:
        heappush(abs_q, (abs(x), x))


for r in result:
    print(r)
