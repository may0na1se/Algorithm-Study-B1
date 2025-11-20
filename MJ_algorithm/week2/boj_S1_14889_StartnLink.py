import sys
# input = sys.stdin.readline
sys.stdin = open('1003/input.txt', 'r')


n = int(input())
stats = [list(map(int, input().split())) for _ in range(n)]

min_difference = 10**8

def calculate_team_stats(team):
    total_stat = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            member1 = team[i]
            member2 = team[j]
            total_stat += stats[member1][member2] + stats[member2][member1]
    return total_stat

def find_teams(start_index, team):
    global min_difference  #프로그래머스 같은 곳에서는 nonlocal 써야되는거같음

    #종료 조건 팀원 수가 N/2
    if len(team) == n // 2:
        # 스타트 팀이 정해지면 나머지가 링크팀
        start_team = team
        link_team = [i for i in range(n) if i not in start_team]
        
        start_stats = calculate_team_stats(start_team)
        link_stats = calculate_team_stats(link_team)
        min_difference = min(min_difference, abs(start_stats - link_stats))
        return

    for i in range(start_index, n):
        team.append(i)
        find_teams(i + 1, team)
        team.pop()


find_teams(0, [])
print(min_difference)

