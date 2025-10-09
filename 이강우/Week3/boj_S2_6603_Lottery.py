'''
문제: https://www.acmicpc.net/problem/6603
접근: 그냥 부분 조합 문제. 여러 줄 입력에 대해서 좀 애먹음

시간복잡도: 이게 어떻게 되는 거드라
'''

def func(cnt=0, prev=1, temp=[]):
    if cnt + (len(inp) - prev) < 6 :
        return
    if cnt == 6:
        a = temp.copy()
        unions.append(a)
        return

    for i in range(prev, len(inp)):
        temp.append(inp[i])
        func(cnt + 1, i+1, temp)
        temp.pop()

while True:
    inp = [*map(int, input().split())]

    k = inp[0]

    if not k:
        break

    unions = []

    func()

    for union in unions:
        print(*union)
    print()
