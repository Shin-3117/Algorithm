#2×n 타일링
# 1 1
# 2 2
# 3 3
# 4 5
# 5 8
# 6 13
# 7 21
# 8 34
# 9 55

N = int(input())
dp = [0]*1001 #(n+1)로 하면 n=1일때 dp[2]가 에러남
dp[1]=1
dp[2]=2
for idx in range(3,N+1):
    dp[idx] = (dp[idx-1] + dp[idx-2])%10007
print(dp[N])