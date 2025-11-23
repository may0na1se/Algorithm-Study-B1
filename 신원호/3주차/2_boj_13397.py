def able(limit):
    now = 0 # 현재 구간 수
    temp_min = 10001
    temp_max = 0
    for num in series:
        if num > temp_max:
            temp_max = num
        if num < temp_min:
            temp_min = num
        if temp_max - temp_min > limit:
            if now < M - 1:
                now += 1
                temp_min = num
                temp_max = num
            else:  # 이미 최대 구간 수에 도달했는데 수열에 수가 남아있는 경우
                return False
    return True

# binary search
# 최종 점수를 탐색할 값으로 설정하고 해당 값이 실현 가능한지를 판정

N, M = map(int, input().split())
series = list(map(int, input().split()))
upper = max(series) - min(series)
lower = 0
while lower <= upper:
    mid = (lower + upper) // 2
    if able(mid):
        upper = mid - 1
    else:
        lower = mid + 1
print(lower)