import sys
# input = sys.stdin.readline

sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())

num_list =  list(map(int, input().split()))

# print(num_list)

left = 0
right = max(num_list)-min(num_list)

while left <= right :
    mid = (left + right) // 2



    num_section = 1
    cur_min, cur_max = num_list[0], num_list[0]

    for i in range(N):
        cur_min = min(cur_min, num_list[i])
        cur_max = max(cur_max, num_list[i])

        if cur_max - cur_min > mid :
            num_section += 1
            cur_min, cur_max = num_list[i], num_list[i] #현재번호부터 새 구간 시작
            
    if num_section > M :  #M개의 구간보다 더 많이 필요하다는 것은 더 촘촘하게 여러번 잘라야 한다는 것
                        # => 지금의 mid값보다 더 넉넉한 = 큰 값을 가지고 검사해야 된다는 것
        left = mid + 1
    else:
        right = mid - 1

# print(left, mid, right)
print(left)