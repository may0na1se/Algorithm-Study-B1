# boj 2599 수열
# 슬라이딩 윈도우 or 누적합

N, K = list(map(int, input().split()))
degrees = list(map(int, input().split()))
max_degrees = sum(degrees[:K])
temp = max_degrees
for i in range(N - K):
    temp = temp - degrees[i] + degrees[i + K]
    if max_degrees < temp:
        max_degrees = temp
print(max_degrees)