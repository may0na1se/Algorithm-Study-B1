'''
문제: https://www.acmicpc.net/problem/2579
접근: 원호님의 힌트로 DP로 푸는 것이라는 것을 알게 되었다.
그래서 set()을 만들어서 DP로 풀어보았다.
근데 메모리 초과 뜸

시간복잡도: 
'''


def func(cnt, now, total):
    global max_score
    if now == 0:
        max_score = max(max_score, total)
        return
    
    if (cnt, now, total) in dp:
        return
    
    dp.add((cnt, now, total))
    
    if cnt == 2:
        if now - 2 >= 0:
            func(1, now-2, total + scores[now-2])
        else:
            return
    
    else:
        func(2, now-1, total + scores[now-1])
        if now - 2 >= 0:
            func(1, now-2, total + scores[now-2])
        else:
            return
    

S = int(input())
scores = [int(input()) for _ in range(S)]

dp = set()
max_score = 0

func(1, S-1, scores[S-1])
print(max_score)