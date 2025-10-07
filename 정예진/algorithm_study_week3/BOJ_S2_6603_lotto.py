# 접근방법 : 전형적인 조합 만들기 문제!
# 출력 사이에 빈칸 안 내서 틀렸었습니다 ㅋㅋ
# 걸린 시간 : 20분

import sys

def recur(cnt, prev):
    if cnt == 6:
        print(*path)
        return

    for i in range(prev, N):
        if visited[i]:
            continue

        path[cnt] = arr[i]
        visited[i] = 1
        recur(cnt+1, i + 1)
        path[cnt] = 0
        visited[i] = 0


while True:
    value = list(map(int, sys.stdin.readline().split()))
    if value[0] == 0:
        break

    N, arr = value[0], value[1:]
    visited = [0] * N
    path = [0] * 6
    recur(0,0)
    print()
