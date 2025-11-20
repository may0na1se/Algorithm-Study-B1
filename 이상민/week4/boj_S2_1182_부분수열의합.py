n,S = map(int,input().split())
N = [int(x) for x in input().split()]

def a(lst):
    if len(lst) == 1: return [0,*lst]
    past_lst = a(lst[1:])
    return past_lst + [x + lst[0] for x in past_lst]

result = a(N)
result.remove(0)
print(result.count(S))