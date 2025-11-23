# boj 1991 트리 순회
# 제곧내

import sys
def preorder(c='A'):
    if c == '.':
        return
    result1.append(c)
    preorder(tree[ord(c) - A][1])
    preorder(tree[ord(c) - A][2])

def inorder(c='A'):
    if c == '.':
        return
    inorder(tree[ord(c) - A][1])
    result2.append(c)
    inorder(tree[ord(c) - A][2])

def postorder(c='A'):
    if c == '.':
        return
    postorder(tree[ord(c) - A][1])
    postorder(tree[ord(c) - A][2])
    result3.append(c)


N = int(input())
tree = [[] for _ in range(N)]
A = ord('A')
for i in range(1, N + 1):
    node, left, right = sys.stdin.readline().split()
    tree[ord(node) - A] = [node, left, right]
result1 = []
result2 = []
result3 = []
preorder()
inorder()
postorder()
print(''.join(result1))
print(''.join(result2))
print(''.join(result3))