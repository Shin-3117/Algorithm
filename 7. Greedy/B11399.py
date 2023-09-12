N = int(input())
lst = list(map(int,input().split()))
lst.sort()
answer = 0

for i in range(N):
    answer += lst[i]*(N-i)

print(answer)