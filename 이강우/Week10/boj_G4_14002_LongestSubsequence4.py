'''
문제: https://www.acmicpc.net/problem/14002
접근: 기본적인 접근방법은 이분탐색 가장 긴 증가하는 부분수열 구하기와 같음
부분 수열을 순서대로 출력하기 위하여 길이를 저장히는 list1 외에,
해당 숫자가 어느 index에 들어가야 가장 유리한 지와 숫자를 함께 기록하는 list2를 만들어주기
가장 긴 부분 수열 list2를 활용하여 구할 수 있음

시간복잡도: O(NlogN) + O(N) = O(NlogN) 이라고 한다
'''

N = int(input())
A = list(map(int, input().split()))

lst = [A[0]]
result = [(0, A[0])]

for i in range(1, N):
    if lst[-1] < A[i]:
        lst.append(A[i])
        result.append((len(lst) - 1, A[i]))
    else:
        left, right = 0, len(lst) - 1
        idx = 0

        while left <= right:
            mid = (left + right) // 2

            if lst[mid] >= A[i]:
                idx = mid
                right = mid - 1
            else:
                left = mid + 1
        lst[idx] = A[i]
        result.append((idx, A[i]))

subsequence = [0] * len(lst)

target = len(lst) - 1
for n in range(len(result) - 1, -1, -1):
    index, val = result[n]
    if index == target:
        subsequence[index] = val
        target -= 1

# print(lst)
# print(result)
print(len(lst))
print(*subsequence)
