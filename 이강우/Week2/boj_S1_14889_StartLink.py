'''
문제: https://www.acmicpc.net/problem/14889
접근: 완전탐색, swea 요리사 문제와 동일함
주의 사항 재귀호출 할 때 prev + 1로 넣어서 계속 시간초과 났었음
i + 1로 넣어야 한다

시간복잡도: 왜 이렇게 계산하기 힘든지...
'''


def team_select(prev, selected, cnt):
    global min_diff
    if cnt == N//2:
        A = 0
        B = 0
        for i in range(N):
            for j in range(i+1, N):
                if i in selected and j in selected:
                    A += synergies[i][j] + synergies[j][i]
                elif i not in selected and j not in selected:
                    B += synergies[i][j] + synergies[j][i]
        min_diff = min(min_diff, abs(A-B))
        return


    for i in range(prev, N):
        if i in selected:
            continue
        selected.add(i)
        team_select(i + 1, selected, cnt + 1)
        selected.remove(i)


N = int(input())
synergies = [list(map(int, input().split())) for _ in range(N)]

min_diff = 21e8

team_select(1, set({0}), 1)

print(min_diff)
