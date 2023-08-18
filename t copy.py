import sys
from collections import deque
import pprint
sys.stdin = open('./inputs/B_13460.txt','r', encoding='utf-8')
input = sys.stdin.readline
I,J = map(int,input().split())
G = [list(input().strip()) for _ in range(I)]
di, dj = [-1,0,1,0], [0,1,0,-1]

sol = -1
ri,rj,bi,bj = 0,0,0,0
for i in range(I):
    for j in range(J):
        if G[i][j] == 'R':
            ri = i
            rj = j
        elif G[i][j] == 'B':
            bi = i
            bj = j
def bfs(ri,rj,bi,bj):
    q = deque()
    q.append([ri,rj,bi,bj])
    visited = []
    visited.append([ri,rj,bi,bj])
    cnt = 0
    while q:
        for _ in range(len(q)):
            if cnt > 10 : 
                print(-1)
                return
            ri,rj,bi,bj = q.popleft()
            if G[ri][rj] == 'O':
                print(cnt)
                return
            for k in range(4):
                rii = ri
                rjj = rj
                while True:
                    rii += di[k]
                    rjj += dj[k]
                    if G[rii][rjj] == '#':
                        rii -= di[k]
                        rjj -= dj[k]
                        break
                    if G[rii][rjj] == 'O':
                        break
                bii = bi
                bjj = bj
                while True:
                    bii += di[k]
                    bjj += dj[k]
                    if G[bii][bjj] == '#':
                        bii -= di[k]
                        bjj -= dj[k]
                        break
                    if G[bii][bjj] == 'O':
                        break
                #
                if G[bii][bjj] == 'O':
                    continue
                # 구슬의 위치가 같다면
                if rii == bii and rjj == bjj:
                    # 늦게온 구슬을 뒤로 이동
                    if abs(rii-ri)+abs(rjj-rj) > abs(bii-bi)+abs(bjj- bj):
                        rii -= di[k]
                        rjj -= dj[k]
                    else:
                        bii -= di[k]
                        bjj -= dj[k]
                # 방문한적이 없으면 큐 추가, 방문 처리
                if [rii,rjj,bii, bjj] not in visited:
                    q.append([rii,rjj,bii,bjj])
                    visited.append([rii,rjj,bii,bjj])
        cnt += 1
    print(-1)

bfs(ri,rj,bi,bj)