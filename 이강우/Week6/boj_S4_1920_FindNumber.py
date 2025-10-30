'''
문제: https://www.acmicpc.net/problem/1920
접근: DAT?였나 하는 방식으로 풀어보려 했으나, 리스트의 크기가 너무 커지는 것 같음 > 바로 메모리 초과
그래서 그냥 set로 받아서 풀었음

시간복잡도: O(M) > M의 수만큼 set에서 찾아야 하니까
'''

N = int(input())
ints = set(map(int, input().split()))


M = int(input())
to_be_founds = list(map(int, input().split()))

for num in to_be_founds:
    if num in ints:
        print(1)
    else:
        print(0)