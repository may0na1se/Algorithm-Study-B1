import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
operators = list(map(int, sys.stdin.readline().split()))
min_val = float('inf')
max_val = float('-inf')

def recur(cnt, total, plus, minus, mul, div):
    global max_val
    global min_val

    if cnt == N:
        min_val = min(min_val, total)
        max_val = max(max_val, total)
        return

    if plus > 0:
        recur(cnt+1, total + numbers[cnt], plus-1, minus, mul, div)
    if minus > 0:
        recur(cnt + 1, total - numbers[cnt], plus, minus-1, mul, div)
    if mul > 0:
        recur(cnt + 1, total * numbers[cnt], plus, minus, mul-1, div)
    if div > 0:
        recur(cnt + 1, int(total / numbers[cnt]), plus, minus, mul, div - 1)

recur(1, numbers[0], operators[0], operators[1], operators[2], operators[3])

print(max_val)
print(min_val)

##  연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다.
## 또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.
# -> 그래서 -10e8, 10e8로 하면 틀림. 왜냐면 같을 수도 있거든