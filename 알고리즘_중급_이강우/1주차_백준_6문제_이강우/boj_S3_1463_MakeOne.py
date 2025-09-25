'''
링크: https://www.acmicpc.net/problem/1463
접근법: 완전탐색 돌려서, 가장 작은 cnt 찾기
만약 중간에 min_oper보다 커지면 return

시간복잡도: ?
'''

def div_three(num):
    return num // 3

def div_two(num):
    return num // 2

def minus(num):
    return num - 1


def func(num, cnt):
    global min_oper
    if cnt >= min_oper:
        return
    if num == 1:
        min_oper = min(min_oper, cnt)
        return

    if not num % 3:
        func(div_three(num), cnt + 1)
    if not num % 2:
        func(div_two(num), cnt + 1)
    func(minus(num), cnt + 1)

N = int(input())
min_oper = 21e8

func(N, 0)

print(min_oper)