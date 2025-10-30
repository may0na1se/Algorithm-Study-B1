# boj 2577 숫자의 개수
# 단순구현

count_list = [0] * 10
num_list = []
for _ in range(3):
    num_list.append(int(input()))
num_multi = 1
for num in num_list:
    num_multi *= num
num_multi_digit = list(map(int,list(str(num_multi))))
for digit in num_multi_digit:
    count_list[digit] += 1
for count in count_list:
    print(count)