# 백트래킹
def calc(s, n=0):
    if n == N - 1:
        result.append(s)
        return
    if condition[0]:
        condition[0] -= 1
        calc(s + nums[n + 1], n + 1)
        condition[0] += 1
    if condition[1]:
        condition[1] -= 1
        calc(s - nums[n + 1], n + 1)
        condition[1] += 1
    if condition[2]:
        condition[2] -= 1
        calc(s * nums[n + 1], n + 1)
        condition[2] += 1
    if condition[3]:
        condition[3] -= 1
        calc(divide(s, nums[n + 1]), n + 1)
        condition[3] += 1

# 나눗셈 연산자만 함수로 만들어서 사용
def divide(a, b):
    if a >= 0:
        return a // b
    return -(abs(a) // b)

N = int(input())
nums = list(map(int, input().split()))
condition = list(map(int, input().split()))
result = []
calc(nums[0])
print(max(result))
print(min(result))