N = int(input())

num_list = list(map(int, input().split()))

pl, mi, mul, div = map(int, input().split())

opers = [0] * pl + [1] * mi + [2] * mul + [3] * div

# print(opers)


oper_stack = []

min_ = 10**9
max_ = -1 * 10**9
visited = [0] * (N-1)
def pick(row, N):
    global min_
    global max_

    if row == N-1:
         
        m = num_list[0]
        for i in range(len(oper_stack)):
            if oper_stack[i] == 0 :
                m += num_list[i+1]
            elif oper_stack[i] == 1 :
                m -= num_list[i+1]
            elif oper_stack[i] == 2 :
                m = m * num_list[i+1]
            elif oper_stack[i] == 3 :
                if m >= 0 :
                    m = m // num_list[i+1]
                else:
                    m = -1 * (-1*m // num_list[i+1])
        # print(oper_stack, m)

        if m >= max_ :
            max_ = m
        if m <= min_ :
            min_ = m

        return 
    
    for i in range(N-1):
        if visited[i] == 1 :
            continue

        oper_stack.append(opers[i])
        visited[i] = 1
    
        pick(row+1, N)        
        visited[i] = 0
        oper_stack.pop()



pick(0, N)
print(max_)
print(min_)