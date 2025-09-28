'''
문제: https://www.acmicpc.net/problem/2579
접근: 약간 Greedy 같은 규칙 적용하면 되지 않을까 싶은데, 구현을 못하겠음
아마 계단 수가 달라지거나 하면, Greedy가 깨지는 듯
S가 300이니까 재귀는 당연히 아니고...

시간복잡도: 
'''


def func(cnt, now, total):
    if now == S-1:
        return total
    
    
    
    pass


S = int(input())
scores = [int(input()) for _ in range(S)]

a = func(1, 0, scores[0])
b = func(1, 1, scores[1])

print(max(a, b))