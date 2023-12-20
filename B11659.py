import sys
sys.stdin = open('./inputs3/B11659.txt','r')
input = sys.stdin.readline

N, M = map(int,input().split())
N_List = list(map(int, input().split()))

sum_stack = [0]*(N+1)
for idx in range(N):
  sum_stack[idx+1] = sum_stack[idx] + N_List[idx]

for _ in range(M):
  i,j = map(int, input().split())
  ans = sum_stack[j]-sum_stack[i-1]
  print(ans)

#부분합