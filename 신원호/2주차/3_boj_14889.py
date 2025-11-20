# SWEA 음식 만들기랑 비슷한 유형의 문제
# 단 이 경우, N이 항상 짝수이고 정확하게 반으로 분할해야 한다.


def make_team(num=0, a=[], b=[]):
    if N // 2 == len(a) == len(b):
        team_case.append((tuple(a), tuple(b)))
        return
    if len(a) < N // 2:
        a.append(num)
        make_team(num + 1, a, b)
        a.pop()
    if len(b) < N // 2:
        b.append(num)
        make_team(num + 1, a, b)
        b.pop()

N = int(input())
status = [list(map(int, input().split())) for _ in range(N)]
result = float('inf')
team_case = []
make_team()
# for team_a, team_b in team_case[: len(team_case) // 2 + 1]:
# 경우의 수 중 절반은 같은 경우이므로 이렇게 하면 시간 절반 단축 가능
for team_a, team_b in team_case:
    synergy_a, synergy_b = 0, 0
    for player in team_a:
        for teammate in team_a:
            synergy_a += status[player][teammate]
    for player in team_b:
        for teammate in team_b:
            synergy_b += status[player][teammate]
    if synergy_a - synergy_b == 0:
        result = 0
        break
    if result > abs(synergy_a - synergy_b):
        result = abs(synergy_a - synergy_b)
print(result)