B = [0]*1001
B[1:3]=1,3
n = int(input())
for i in range(3,n+1):
    B[i]+=2*B[i-2]+B[i-1]

print(B[n]%10007)