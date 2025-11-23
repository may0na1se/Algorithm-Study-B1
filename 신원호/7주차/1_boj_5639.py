# boj 5639 이진 검색 트리
# 전위 순회한 결과로 원본 트리를 복원
# 전위 순회 결과의 0번 인덱스가 루트노드
# 완전 편향트리일 경우가 최악의 케이스 -> 재귀횟수 N번

import sys
sys.setrecursionlimit(10**5)

preorder = []
while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except ValueError:
        break

def postorder(start, end):
    if start > end:
        return
    root = preorder[start]
    mid = start + 1
    while mid <= end and preorder[mid] < root:
        mid += 1
    postorder(start + 1, mid - 1)
    postorder(mid, end)
    print(root)

postorder(0, len(preorder) - 1)