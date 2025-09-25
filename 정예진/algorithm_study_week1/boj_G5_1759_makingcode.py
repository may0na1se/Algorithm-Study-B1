# “모음 조합”과 “자음 조합”을 각각 재귀로 찾음
# 조건에 맞게 합쳐서 최종 문자열 출력

import sys

L, C = map(int, sys.stdin.readline().split())
alpha_ls = sys.stdin.readline().split()
vowel_ls = list()
consonant_ls = list()

for i in range(len(alpha_ls)):
  if alpha_ls[i] in 'aeiou':
    vowel_ls.append(alpha_ls[i])
  else:
    consonant_ls.append(alpha_ls[i])

vowel_ls.sort()
consonant_ls.sort()

visited = [0] * L
path = list()

def recur(cnt, X, start, leng, ls):
  num_ls = [i for i in range(leng)]
  if cnt == X:
    ls.append(path[:])
    return
  
  for i in range(start, leng):
      path.append(num_ls[i])
      recur(cnt+1, X, i+1, leng, ls)
      path.pop()

ans_ls = set()
for a in range(1, L-2+1):
    b = L - a
    vowel = list()
    consnt = list()
    recur(0, a, 0, len(vowel_ls), vowel)
    recur(0, b, 0, len(consonant_ls), consnt)
    
    for v in vowel:
        for c in consnt:
            ans = list()
            for wv in v:
                ans.append(vowel_ls[wv])
            for wc in c:
                ans.append(consonant_ls[wc])
            ans.sort()
            ans_ls.add(''.join(ans))

answer = list(ans_ls)
answer.sort()

for a in answer:
    print(a)