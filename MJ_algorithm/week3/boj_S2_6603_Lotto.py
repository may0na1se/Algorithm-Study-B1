import sys
# input = sys.stdin.readline

sys.stdin = open('input.txt', 'r')

while True:

    input_list = list(map(int, input().split()))
    if input_list == [0]:
        break

    k, S = input_list[0], input_list[1:]

    # print(S)



    result = []
    def pick(row):
        if len(result) == 6 :
            print(*result)
            return
        
        for i in range(row, k):
            result.append(S[i])
            pick(i + 1)
            result.pop()
            

    pick(0)
    print('')