# 접근 방법 : 츄러스랑 비슷하게 접근하되, cnt와 l,r 옮기는 조건만 좀 다르게 가면 된다
# 츄러스처럼 이진탐색으로 접근, cnt에 더할 때 개수가 아니라 도시별 예산을 더해준다고 생각하면 됨
# mid가 모든 도시에 대한 예산이고, 만약 city가 요구하는 예산이 mid보다 작으면 요구한 값만 주면 되기 때문에
# cnt에 더할 때 min(city, mid)로 누적합
# cnt가 전체 예산보다 크면 r을 옮기고 아니면 l을 옮겨서 가장 최적의 값 찾아내기
# 풀이시간 : 30분
import sys

N = int(sys.stdin.readline())
budgets = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

l, r = 1, max(budgets)
while l <= r:
    mid = (l+r) // 2
    cnt = 0
    for city in budgets:
        cnt += min(city, mid)
    if cnt > M:
        r = mid - 1
    else:
        l = mid + 1

print(r)