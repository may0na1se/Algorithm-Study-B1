import sys


sys.stdin = open('input.txt', 'r', encoding='utf-8-sig')
input = sys.stdin.readline

N = int(input())

size = []
rank_list = []
for _ in range(N):
    x, y = map(int, input().split())
    size.append((x,y))

for i in range(N):
    
    k = 0  #나보다 덩치 큰 사람의 수
    
    for j in range(N): 
        if size[i][0] < size[j][0] and size[i][1] < size[j][1]:
            k += 1
    
    rank_list.append(k+1)

print(*rank_list)