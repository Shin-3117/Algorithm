import sys
sys.stdin = open('./inputs2/S16938.txt','r')

def backTracking(i,j,s):
    global sol
    if i >= N:
        if sol > s : 
            sol = s
            return
    if sol < s:
        return

    for k in range(N):
        if visited[k] == 0:
            visited[k] = 1
            s += MAP[i][k]
            backTracking(i+1,k,s)
            visited[k] = 0
            s -= MAP[i][k]


for test_case in range(1,int(input())+1):
    N = int(input())
    MAP = [list(map(int,input().split())) for _ in range(N)]
    visited = [0]*N
    sol=float('inf')
    for i in range(N):
        visited[i] = 1
        backTracking(1,i,MAP[0][i])
        visited[i] = 0

    print(f'#{test_case} {sol}')