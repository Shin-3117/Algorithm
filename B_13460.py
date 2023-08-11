import sys
from collections import deque

import pprint
sys.stdin = open('./inputs/B_13460.txt','r', encoding='utf-8')

input = sys.stdin.readline
I,J = map(int,input().split())
G = []
for i in range(I):
    # 그래프 입력 받기
    G.append(list(input().strip()))
    # R,B 위치 찾기
    for j in range(J):
        if G[i][j] == 'R':
            Ri,Rj = i,j
        elif G[i][j] == 'B':
            Bi,Bj = i,j

di, dj = [-1,0,1,0], [0,1,0,-1]

def bfs(Ri,Rj,Bi,Bj):
    q = deque()
    q.append((Ri,Rj,Bi,Bj))
    visited = []
    # 방문처리
    visited.append((Ri,Rj,Bi,Bj))
    count = 0
    while q:
        for _ in range(len(q)):
            Ri,Rj,Bi,Bj = q.popleft()
            if count > 10 : 
                print(-1)
                return
            # 빨간 구슬이 도착 한 경우 카운트 출력
            if G[Ri][Rj] == 'O':
                print(count)
                return
            for k in range(4):
                # 한 방향 탐색 후, 초기화
                nRi = Ri
                nRj = Rj
                # R 한 방향으로 쭉 가기
                while True:
                    nRi +=di[k]
                    nRj +=dj[k]
                    # 벽인 경우 왔던 방향 그대로 한칸 뒤로 이동
                    if G[nRi][nRj] == '#': 
                            nRi -= di[k]
                            nRj -= dj[k]
                            break
                    # O에 도착
                    if G[nRi][nRj] == 'O': break
                # 한 방향 탐색 후, 초기화
                nBi = Bi
                nBj = Bj
                # B 한 방향으로 쭉 가기
                while True:
                    nBi += di[k]
                    nBj += dj[k]
                    # 벽인 경우 왔던 방향 그대로 한칸 뒤로 이동
                    if G[nBi][nBj] == '#': 
                            nBi -= di[k]
                            nBj -= dj[k]
                            break
                    # O에 도착
                    if G[nBi][nBj] == 'O': break
                # 이동 완료 후
                # 파란구슬이 먼저 구멍에 들어가거나 동시에 들어가면 안됨 따라서 이 경우 무시
                if G[nBi][nBj] == 'O': continue
                # 구슬의 위치가 같다면
                if nRi == nBi and nRj == nBj:
                    # 늦게온 구슬을 뒤로 이동
                    if abs(nRi-Ri)+abs(nRj-Rj) > abs(nBi-Bi)+abs(nBj-Bj):
                        nRi -= di[k]
                        nRj -= dj[k]
                    else:
                        nBi -= di[k]
                        nBj -= dj[k]
                # 방문한적이 없으면 큐 추가, 방문 처리
                if (nRi,nRj,nBi,nBj) not in visited:
                    q.append((nRi,nRj,nBi,nBj))
                    visited.append((nRi,nRj,nBi,nBj))
        count +=1
    # 10회를 초과하지 않았지만, 10회 내에도 구멍에 들어가지 못하는 경우(이동불가)
    print(-1)

bfs(Ri,Rj,Bi,Bj)