# 접근 방법 : heapq 이용, push할 때는 abs와 기존 값 함께 넣어주고 pop 해서 프린트할 때는 기존값만 출력

import sys
from heapq import heappop, heappush

data = list(map(int, sys.stdin.read().split()))
N = data[0]
data = data[1:]
ls = list()

for val in data:
    if val == 0:
        if ls:
            a = heappop(ls)
            print(a[1])
        else:
            print(0)
    else:
        heappush(ls, (abs(val),val))