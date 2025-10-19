'''
문제: https://www.acmicpc.net/problem/2512
접근: 총 예산을 배정해야하는 개수만큼 나눠서 limit를 정한다.
평균 예산보다 큰 애들을 세주고, 평균 예산보다 작은 애들을 평균 예산에서 빼서 남는 예산을 구한다.
그리고 만약 총 요구가 예산보다 더 크다면, (남는 예산 // 평균보다 큰 애들 수)를 해줘서 평균 예산에 더해서 답을 구한다.
반례:
4
122 110 140 150
485
정답이 125가 나와야 하는데, 내 구성대로라면 밑을 그냥 버리기 때문에, 124가 나온다

시간복잡도:
'''

N = int(input())

required = sorted(list(map(int, input().split())))

budget = int(input())

limit = budget // N

over_cnt = 0
remaining = 0

for i in range(N):
    if required[i] > limit:
        over_cnt += 1
    else:
        remaining += limit - required[i]


if sum(required) < budget:
    print(required[-1])
else:
    print(limit + remaining//over_cnt)