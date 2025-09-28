# 재귀
def password(n=0, start=0, char='', count_c=0, count_v=0):
    # 모음 자음 조건을 만족할 경우 출력
    if n == L :
        if count_c >= 2 and count_v >= 1:
            print(char)
        return
    for i in range(start, C):
        if letter[i] in vowel:
            password(n + 1, i + 1, char + letter[i], count_c, count_v + 1)
        else:
            password(n + 1, i + 1, char + letter[i], count_c + 1, count_v)
# 모음
vowel = {'a', 'e', 'i', 'o', 'u'}
L, C = map(int, input().split())
# 알파벳 순으로 정렬
letter = sorted(input().split())
password()