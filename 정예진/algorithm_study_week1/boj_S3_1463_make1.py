#X가 3으로 나누어 떨어지면, 3으로 나눈다.
#X가 2로 나누어 떨어지면, 2로 나눈다.
#1을 뺀다.

# import sys
# N = int(sys.stdin.readline())

# cnt = [[]] * N
# cnt[0] = [N]
# i = 1

# while True:
#     for num in cnt[i-1]:
#         if N % 3 == 0:
#             cnt[i] += [N//3]

#         if N % 2 == 0:
#             cnt[i] += [N//2]
    
#         cnt[i] += [N - 1]

#     if 1 in cnt[i]:
#         break
#     else:
#         i += 1

# print(i)



import sys

N = int(sys.stdin.readline())


cnt = [0 for _ in range(N+1)]

for i in range(2, N+1):
    cnt[i] = cnt[i-1] + 1
    
    if i % 2 == 0:
        cnt[i] = min(cnt[i], cnt[i//2] + 1)
    
    if i % 3 == 0:
        cnt[i] = min(cnt[i], cnt[i//3] + 1)
        
print(cnt[N])