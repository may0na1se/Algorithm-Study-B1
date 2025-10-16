# 접근 방법 : DP.. 너무 어려워요...
# 지난주 원호오빠가 썼던 것처럼 2차원 DP 테이블을 만들어서 물건 개수와 무게를 각각 행,열로 넣고
# 가치를 cell의 값으로 넣었습니다
# 걸린 시간 : 약 80분?

import sys

N, K = map(int, sys.stdin.readline().split())
items = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

# DP 테이블 초기화 (행: 물건 개수, 열: 무게 한도)
dp = [[0] * (K + 1) for _ in range(N + 1)]

# DP 채우기
for i in range(1, N + 1):          # 1번째 ~ N번째 물건
    w, v = items[i - 1]            # 현재 물건의 무게, 가치
    for k in range(1, K + 1):      # 무게 한도 1~K
        if k < w:                  # 현재 물건을 담을 수 없으면 지금 물건 무시, 이전 row의 값 그대로
            dp[i][k] = dp[i - 1][k]    
        else:                      # 담을 수 있다면 담는 경우 고려 (지금 물건의 가치 + 남은 무게(k-w)로 가능한 최대 가치)
            dp[i][k] = max(dp[i - 1][k], dp[i - 1][k - w] + v)

print(dp[N][K])
