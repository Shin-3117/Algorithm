import sys
sys.stdin = open('./inputs/S_2117.txt','r')
#2117. [모의 SW 역량테스트] 홈 방범 서비스
"""
1. 시간제한 : 최대 50개 테스트 케이스를 모두 통과하는데, C/C++/Java 모두 3초
2. 도시의 크기 N은 5 이상 20 이하의 정수이다. (5 ≤ N ≤ 20)
3. 하나의 집이 지불할 수 있는 비용 M은 1 이상 10 이하의 정수이다. (1 ≤ M ≤ 10)
4. 홈방범 서비스의 운영 비용은 서비스 영역의 면적과 동일하다.
5. 도시의 정보에서 집이 있는 위치는 1이고, 나머지는 0이다.
6. 도시에는 최소 1개 이상의 집이 존재한다.
 K * K + (K - 1) * (K - 1)
"""
from collections import deque
di,dj = [1,-1,0,0],[0,0,1,-1]
def bfs(i,j):
    global sol
    q=deque()
    q.append([i,j])
    C[i][j] = 1

    home = G[i][j]
    if sol < home:
        sol = home
    K = 1
    while q:
        K+=1
        # K 범위 별로 돔
        for _ in range(len(q)):
            ni,nj = q.popleft()
            for move in range(4):
                ii = ni+di[move]
                jj = nj+dj[move]
                if 0<=ii<N and 0<=jj<N and C[ii][jj] == 0:
                        q.append([ii,jj])
                        C[ii][jj] = 1
                        home += G[ii][jj]
            
        if M*home - (K*K + (K-1)*(K-1)) >=0:
            if sol < home:
                sol = home

T = int(input())
for tc in range(T):
    N,M = map(int, input().split())
    G = [list(map(int,input().split())) for _ in range(N)]
    sol = 0
    for i in range(N):
        for j in range(N):
            C = [[0]*N for _ in range(N)]
            bfs(i,j)
    print(f'#{tc+1} {sol}')