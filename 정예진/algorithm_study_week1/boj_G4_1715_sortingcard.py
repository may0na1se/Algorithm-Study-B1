import sys
from heapq import heappop, heappush, heapify

N = int(sys.stdin.readline())
numbers = [0 for _ in range(N)]
for n in range(N):
    numbers[n] = int(sys.stdin.readline())
heapify(numbers)

if len(numbers) == 1:
    print(0)
else:
    res = heappop(numbers) + heappop(numbers)
    result = res
    while numbers:
        heappush(numbers, res)
        res = heappop(numbers) + heappop(numbers)
        result += res

    print(result)