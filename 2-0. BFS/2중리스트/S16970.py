import sys
sys.stdin = open('./inputs2/S16970.txt','r')
"""
10개 테스트 케이스, 3초
3<=N<=100, 0<=H<1000

DFS : O(V+E)=30000
#E=2V V=N*N=10000
예상 시간 : DFS * 테스트케이스 = 30000*10 = 150_0000+@ < 3억, time in
하지만 time out
BFS는 패스
"""
from collections import deque
moves = [(1,0),(0,1),(-1,0),(0,-1)]
def bfs():
    q =deque()
    q.append((0,0))
    while q:
        i,j = q.popleft()
        for move in moves:
            ii = i + move[0]
            jj = j + move[1]
            if 0<=ii<graphSize and 0<=jj<graphSize:
                # 더 높은 곳으로 이동
                up=0
                if graph[ii][jj] > graph[i][j]:
                    up = graph[ii][jj] - graph[i][j]

                if Sgraph[ii][jj] !=0:
                    if Sgraph[ii][jj] > Sgraph[i][j]+1+up:
                        Sgraph[ii][jj] = Sgraph[i][j]+1+up
                        q.append((ii,jj))
                else:
                    Sgraph[ii][jj] = Sgraph[i][j]+1+up
                    q.append((ii,jj))

for testCase in range(int(input())):
    graphSize = int(input())
    graph = [list(map(int,input().split())) for _ in range(graphSize)]
    Sgraph = [[0]*graphSize for _ in range(graphSize)]
    bfs()
    sol = Sgraph[graphSize-1][graphSize-1]
    print(f'#{testCase+1} {sol}')