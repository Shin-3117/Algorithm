# https://www.acmicpc.net/problem/1012
"""
1. Idea
2중 포문으로 돌면서 1찾기
찾으면 정답+1
BFS로 인접1도 처리

2. 시간 복잡도 BFS:O(V+E) = 5 N*M
V : N*M
E : V*4

3. 자료구조
data : int[][]
chk : boolean[][]
sol : int
"""
import sys
from collections import deque
sys.stdin = open('./inputs/B_1012.txt','r', encoding='utf-8')
for _ in range(int(sys.stdin.readline())):
    N,M,K = map(int,sys.stdin.readline().split())
    data = [[0]*M for _ in range(N)]
    for _ in range(K):
        i, j = map(int,sys.stdin.readline().split())
        data[i][j] = 1
    
    di,dj =[-1,1,0,0], [0,0,-1,1]

    def bfs(i,j):
        rs = 1
        q =deque()
        q.append((i,j))
        while q:
            i,j = q.popleft()
            for d in range(4):
                ii=i+di[d]
                jj=j+dj[d]
                if 0<=ii<N and 0<=jj<M and data[ii][jj] == 1:
                    data[ii][jj] = 0
                    rs +=1
                    q.append((ii,jj))
        return rs
    sol = 0
    for i in range(N):
        for j in range(M):
            if data[i][j] == 1:
                data[i][j] = 0
                sol +=1
                bfs(i,j)

    print(sol)
