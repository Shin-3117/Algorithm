import sys
sys.stdin = open('./inputs2/S14889.txt','r')
input = sys.stdin.readline
N = int(input())
G = [list(map(int,input().split())) for _ in range(N)]

sol = 0
visited = [0]*N

sol = float('inf')

def dfs(v,l):
    global sol
    if l == N//2:
        a=0
        b=0
        for i in range(N):
            for j in range(N):
                if visited[i] == 1 and visited[j] == 1:
                    a+= G[i][j]
                elif visited[i] == 0 and visited[j] == 0:
                    b+= G[i][j]
        # print(abs(a-b))
        sol = min(sol,abs(a-b)) 
        return
    
    
    for nv in range(v,N):
        if visited[nv] == 0:
            visited[nv] = 1
            dfs(nv,l+1)
            visited[nv] = 0

dfs(0,0)

print(sol)