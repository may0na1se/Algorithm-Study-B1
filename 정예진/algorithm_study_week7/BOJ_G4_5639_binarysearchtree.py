# 접근 방법 : 재귀로 그래프 순회하기! 어디에서 재귀를 들어갈지 가치 뻗어나갈 곳 조건 정하는 게 어려웠음 ㅜ
# 소요 시간 : 40분? 

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.read().split()

ls = list(map(int, input))

def recur(start, end):
    if start > end:
        return

    root = ls[start]  # 시작을 root로 정하기
    split_idx = end+1  # 일단 나누는 곳은 제일 끝으로 설정

    for i in range(start+1, end+1):
        if ls[i] > root:  # root보다 크다 -> 오른쪽 서브트리의 시작 (전위순회에서는)
            split_idx = i  # 그래서 이거를 나뉘는 곳으로 설정 -> 각 서브트리에 대해 모두 수행
            break
    # root의 왼쪽 서브트리
    recur(start+1, split_idx-1)
    # root의 오른쪽 서브트리
    recur(split_idx, end)
    print(root)  # 우리가 해야하는 건 후위순회로 출력하기임 그래서 전위순회로 쭉 돈 걸 반대로 출력하면 후위순회가 된다

recur(0, len(ls)-1)