import sys
sys.stdin = open('input.txt', 'r')

N, M, L = map(int, input().split())
pos = list(map(int, input().split()))

pos = pos + [0] + [L]
pos.sort()

# print(pos)

def check_gap(mid):
    stop_count = 0
    for dist in dists:
        if dist > mid :
            stop_count += (dist-1) // mid
            #0 ~ 100 사이, 미드가 50 이라면 1개 필요 
            #0 ~ 101, 미드 50 이라면 2개  101 - 1 // 50
    
    if stop_count <= M : #주어진 M개 휴게소를 더 지어서 mid만큼의 거리를 만족가능하다면, 간격을 더 줄여보기. 
        #안된다면 거리를 늘이기
        return True
    else:
        return False
    
dists = []
for i in range(0, N+1):
    dists.append(pos[i+1]-pos[i])    

# print(dists)

left = 1
right = L

while left <= right :
    mid = (left + right) // 2 
    
    
    if check_gap(mid) == True:
        right = mid - 1
    else:
        left = mid + 1

print(left)