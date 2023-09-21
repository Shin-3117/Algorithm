# https://www.acmicpc.net/problem/1926
# BFS 그래프 이어진영역체크
"""
1. 아이디어
- 2중 for => 값 1 and 미방문 => BFS
- BFS 돌면서 그림 개수 +1, 최대값 갱신
2. 시간복잡도
- BFS : O(V+E)
V=m*n : 500*500
E=V*4(가운대연결된 간선 수) : 4*500*500
V*E : 1250000 >> 125만으로 2억보다 작아서 가능

3. 자료구조
- 그래프 전체 지도 : int[][]
- 방문
- Queue(BFS)
"""
import sys
from collections import deque
sys.stdin = open('./inputs/B_1926.txt','r', encoding='utf-8')
#input() = sys.stdin.readline()
I, J = map(int, sys.stdin.readline().split())
map = [list(map(int,sys.stdin.readline().split())) for _ in range(I)]

visited = [[0]*J for _ in range(I)]
di = [-1,0,1,0]
dj = [0,-1,0,1]

def bfs(i,j):
    size=1
    q = deque([[i,j]])
    # 큐가 빌 때까지 반복
    while q:
        ei, ej = q.popleft()
        # 방향이동
        for k in range(4):
            ii = ei +di[k]
            jj = ej +dj[k]
            # 넘어가지 않게, 그리고 미방문시
            if 0<=ii<I and 0<=jj<J and visited[ii][jj]==0:
                # 이동한 영역이 1(그림) 이면
                if map[ii][jj] == 1:
                    size+=1
                    visited[ii][jj] = 1
                    q.append([ii,jj])
    return size


cnt=0
maxV=0
for i in range(I):
    for j in range(J):
        # map에 1(그림)이 있고 방문한적이 없으면
        if map[i][j] == 1 and visited[i][j] == 0:
            #방문처리
            visited[i][j]=1
            #전체 그림 갯수 를 +1
            cnt+=1
            # BFS로 그림의 크기를 구함
            maxV = max(maxV,bfs(i,j))
            # 최대값 갱신

print(cnt)
print(maxV)