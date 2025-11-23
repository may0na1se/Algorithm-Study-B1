N, M = map(int, input().split())

input_list = input().split()

input_list.sort()
# print(input_list)


result = []
visited = [0] * M
ans = ''

anss = []

vowel = ['a','e','i','o','u']



def pick(row, N, M):
    global ans




    if len(result) == N:
        # print(ans)
        anss.append(ans)
        return


    for i in range(M):
        if visited[i] == 1:
            continue

        if len(result) == 0 or i > result[-1]:
            result.append(i)
            ans += input_list[i]
            visited[i] = 1
            pick(row+1, N, M)
            result.pop()
            ans = ans[:-1]
            visited[i] = 0

pick(0, N, M)


# print(anss)
for answer in anss:
    vowel_count = 0
    consonant_count = 0

    for _ in answer:
        if _ in vowel:
            vowel_count += 1
        else:
            consonant_count += 1
    # print(answer, vowel_count, consonant_count)
    if vowel_count > 0 and consonant_count > 1 :
        print(answer)