# 접근방법 : KKR의 요리사 문제와 동일한? 문제
# N수가 크지 않으니 재귀로 돌립니다 -> 주어진 인원 중 절반 고르는 조합 구하기
# get_synergy : 조합에 있으면 A팀, 없으면 B팀
# calculate : 각 팀별 시너지 계산

import sys

N = int(sys.stdin.readline())
skill = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def calculate(li):
    total = 0
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            total += skill[li[i]][li[j]] + skill[li[j]][li[i]]
    return total

def get_synergy():
    A_ls, B_ls = [], []
    for i in range(N):
        if visited[i]:
            A_ls.append(i)
        else:
            B_ls.append(i)

    return calculate(A_ls), calculate(B_ls)

def recur(cnt, prev):
    global min_val
    if cnt == N//2:
        s,l = get_synergy()
        min_val = min(min_val, abs(s-l))
        return

    for member_number in range(prev+1, N):
        if visited[member_number]:
            continue

        visited[member_number] = 1
        recur(cnt+1, member_number)
        visited[member_number] = 0


visited = [0] * N
min_val = 21e8
recur(0,0)
print(min_val)