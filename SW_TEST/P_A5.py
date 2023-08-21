import sys
sys.stdin = open('./SW_TEST/P_A5.txt','r')
"""
1초
3 <= N, M <= 15
포문 15*15
dfs O(V+E) : V+6V = 7*15*15
7*15*15*15*15 = 354375
"""
from collections import deque
#j가 홀수 일때 이동가능 경로
di1 = [-1,0,0,1,1,1]
dj1 = [0,-1,1,-1,0,1]
#j가 짝수 일때 이동가능 경로
di0 = [-1,-1,-1,0,0,1]
dj0 = [-1,0,1,-1,1,0]

def bfs(i,j):
    q = deque()
    q.append([i,j])
    C[i][j]=True
    move = 0
    # sol = G[i][j]
    while move<5:
        move += 1
        for n in range(len(q)):
            i,j = q.popleft()
            if j%2 ==0:
                for k in range(6):
                    ii = i + di0[k]
                    jj = j + dj0[k]
                    if 0<=ii<I and 0<=jj<J:
                        if C[ii][jj] == False:
                            q.append([ii,jj])
                            C[ii][jj] = True
            else:
                for k in range(6):
                    ii = i + di1[k]
                    jj = j + dj1[k]
                    if 0<=ii<I and 0<=jj<J:
                        if C[ii][jj] == False:
                            q.append([ii,jj])
                            C[ii][jj] = True

T = int(input())
for t in range(T):
    I,J = map(int,input().split())
    G = [list(map(int,input().split())) for _ in range(I)]
    C = [[False]*J for _ in range(I)]

    sol = 0
    
    for i in range(I):
        cnt = 0
        for j in range(J):
            
            bfs(i,j)
            
    print(f'#{t+1} {sol}')
