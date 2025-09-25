X = int(input())




dp = [0] * (X+1)
dp[1] = 0 

i = 2

while i <= X : 
    dp[i] = dp[i-1] + 1

    if i % 2 == 0 :
        dp_2 = dp[i//2]+1
        dp[i] = min(dp[i], dp_2)

    if i % 3 == 0 :
        dp_3 = dp[i //3] + 1 
        dp[i] = min(dp[i], dp_3)


    i += 1

print(dp[X])

