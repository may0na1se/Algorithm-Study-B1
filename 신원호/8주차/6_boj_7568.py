# boj 7568 덩치
# 브루트포스 사용시 O(N^2)
# N <= 50이니 충분히 가능하다.

N = int(input())
people = []
grade = [0] * N
for _ in range(N):
    people.append(list(map(int, input().split())))
for i in range(N):
    count = 1
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            count += 1
    grade[i] = str(count)
print(' '.join(grade))