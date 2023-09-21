import sys
sys.stdin = open("./inputs2/B11047.txt","r")

N, K = map(int,input().split())
coins = [int(input()) for _ in range(N)]
# print(coins)
answer = 0

for i in range(N):
    if K >= coins[-i-1]:
        answer += K//coins[-i-1]
        K = K%coins[-i-1]

print(answer)