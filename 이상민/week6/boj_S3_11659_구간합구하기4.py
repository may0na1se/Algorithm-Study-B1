def init(start,end,node):
    if start==end:
        T[node] = B[start]
        return T[node]
    L = init(start,(start+end)>>1,node*2)
    R = init(((start+end)>>1)+1,end,node*2+1)
    T[node] = L+R
    return L+R

def sum_tree(start,end,node,left,right):
    if left<=start and end<=right: return T[node]
    if end<left or right<start: return 0
    L = sum_tree(start,(start+end)>>1,node*2,left,right)
    R = sum_tree(((start+end)>>1)+1,end,node*2+1,left,right)
    return L+R

N,M = map(int,input().split())
T = [0]*(N*4)
B = [0]+[*map(int,input().split())]

init(1,N,1)
for _ in range(M):
    print(sum_tree(1,N,1,*map(int,input().split())))