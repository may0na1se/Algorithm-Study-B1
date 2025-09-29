# SWEA 츄러스 자르기랑 완전히 같은 문제, 이분 탐색
# lower, upper 헷갈리지 않기

K, N = map(int, input().split())
lan = []
for _ in range(K):
    lan.append(int(input()))
lower = 1
upper = max(lan)
while lower <= upper:
    mid = (lower + upper) // 2
    count = 0
    for line in lan:
        count += line // mid
    if count < N:
        upper = mid - 1
    else:
        lower = mid + 1
print(upper)