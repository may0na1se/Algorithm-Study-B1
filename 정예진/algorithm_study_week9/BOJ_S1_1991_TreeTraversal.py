# 접근 방법 : 트리 순회를 위한 재귀 연습 / 입력을 어떻게 받을 것인지 에 대해서 좀 고민함
# 전위순회 : root - left - right / 중위순회 : left - root - right / 후위순회 : left - right - root
# 재귀로 그냥 돌리면 됨 깊이가 안 깊어서 시간 초과 걱정은 없었음!!
# 소요 시간 : 40분 (중간에 방법 바뀌어서 좀 걸림 ㅜ)
import sys

input = sys.stdin.readlines()

N = int(input[0])
trees = {}

for _ in range(1,N+1):
    root, left, right = input[_].strip().split()
    trees[root] = (left, right)

def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(trees[node][0])
    preorder(trees[node][1])

def inorder(node):
    if node == '.':
        return
    inorder(trees[node][0])
    print(node, end='')
    inorder(trees[node][1])


def postorder(node):
    if node == '.':
        return
    postorder(trees[node][0])
    postorder(trees[node][1])
    print(node, end='')


preorder('A')
print('')
inorder('A')
print('')
postorder('A')
