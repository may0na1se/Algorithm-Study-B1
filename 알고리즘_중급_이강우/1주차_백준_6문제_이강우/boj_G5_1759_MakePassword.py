'''
https://www.acmicpc.net/problem/1759
완전 탐색 돌리면서, 탐색 수를 줄이는 조건 넣어주기

조건
1. 원하는 길이 안 될 때 return
2. prev 넣어줘서 순서 지키고, 이미 들어간 거 안 볼 수 있도록

시간 복잡도: O(N**N)?
'''
 

def func(prev, result, v, c):
    if len(result) == L:
        if v >= 1 and c >= 2:
            print(result)
        return


    for i in range(prev, C):
        if len(result) + (C-prev) < L:
            return
        if characters[i] in ["a", "e", "i", "o", "u"]:
            func(i+1, result + characters[i], v + 1, c)
        else:
            func(i+1, result + characters[i], v, c + 1)
    return


L, C = map(int, input().split())
characters = list(input().split())
characters.sort()

func(0, "", 0, 0)