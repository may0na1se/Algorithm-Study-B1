'''
문제: https://www.acmicpc.net/problem/13397
접근: 그냥 못하겠음~~

시간복잡도:
'''

def func(div, prev):
    global min_diff
    if div < M and prev >= N:
        return

    if div == M:
        unions[M] = (unions[div-1][1], N)
        temp = -21e8
        for j in range(1, M+1):
            start, end = unions[j]
            temp = max(temp, max(lst[start:end]) - min(lst[start:end]))
        min_diff = min(min_diff, temp)
        return
    
    
    
    for i in range(prev, N+1):
        if M-div > N - i:
            continue
        unions[div] = (unions[div-1][1], i)
        func(div+1, i+1)
        unions[div] = 0



N, M = map(int, input().split())

lst = list(map(int, input().split()))

unions = [(0, 0) for _ in range(M+1)]

min_diff = 21e8

func(1, 1)

print(min_diff)