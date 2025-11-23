# 접근 방법 : 이진탐색! 인건 알았음 근데 이걸 어떻게 이진탐색하지? 를 엄청 오래 고민함 ㅜㅜ
# K에 대한 이진탐색인데, 이 K가 전체 일수에 대해 가능한지 확인하는 함수가 하나 추가되면 생각보다 쉽게 풀린다!
import sys
input = sys.stdin.readlines()

N, M = map(int, input[0].split())
money = []
for _ in range(1, N+1):
    money.append(int(input[_].strip()))

def check(k):
    current_money = 0
    cnt = 0
    for idx in range(N):
        if k < money[idx]:
            return False
        if current_money < money[idx]:
            cnt += 1
            current_money = k
        else:
            pass
        current_money -= money[idx]
    if cnt <= M:
        return True
    else:
        return False

l,r = max(money), sum(money)
answer = 0
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        answer = mid
        r = mid - 1
    else:
        l = mid + 1

print(answer)