N = int(input())
nums = list(map(int, input().split()))
sums = [0]
# 연속 음수 구간과 연속 양수 구간으로 정리
for i in range(N):
    if nums[i] >= 0:
        if sums[-1] < 0:
            sums.append(nums[i])
        else:
            sums[-1] += nums[i]
    else:
        if sums[-1] <= 0:
            sums[-1] += nums[i]
        else:
            sums.append(nums[i])
for i in range(1, len(sums)):
    if sums[i - 1] > 0 and sums[i - 1] + sums[i] > 0:
        sums[i] = sums[i - 1] + sums[i]
result = max(sums)
if result < 0:  # nums가 모두 음수인 경우
    result = max(nums)
print(result)
