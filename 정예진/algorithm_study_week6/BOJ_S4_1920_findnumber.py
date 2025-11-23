# 접근법 : 처음에는 dat 느낌으로 가려다가 조건 보고 back 
# 그래서 이진탐색으로 처음 입력 받은 arr을 정렬하고 해당 숫자가 arr 안에 있는지 없는지 탐색
# 풀이 시간 : 20분
import sys

N = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))


def find(x):
    l,r = 0, N-1
    while l <= r:
        mid = (l + r) // 2
        if x == arr[mid]:
            return 1
        elif x > arr[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return 0

for x in numbers:
    print(find(x))


# second solution
# 그냥 arr을 set으로 입력 받기 ㅋㅋ 실행시간이 1/3이 됨
N = int(sys.stdin.readline())
arr = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
for num in list(map(int, sys.stdin.readline().split())):
    if num in arr:
        print(1)
    else:
        print(0)