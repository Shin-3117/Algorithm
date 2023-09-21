import sys
sys.stdin = open('./inputs/S_16494.txt','r', encoding='utf-8')
# BFS로 풀기
# BFS에 사용할 Queue 자료구조 import
from collections import deque

def bfs(G, C, S, E):
    #queue 선언
    q =deque()
    # 시작지점 큐에 넣기
    q.append(S)
    # 방문 처리
    C[S] = True
    # 큐가 빌 때까지 반복
    while q:
        # que에서 index 0 번 자료 뽑기
        v = q.popleft()
        # v에는 갈수있는 노드 리스트가 있음 /[4, 3]
        for i in G[v]:
            # i가 도착 지점과 같다면 1리턴 /i =4
            if i == E:
                return 1
            # G[4]가 비어있지 않고 방문한적이 없으면 /G[4] : [6]
            elif G[i] != [] and C[i] == False:
                # i 큐에 넣기
                q.append(i)
                # 방문처리
                C[i] = True
    # 시작점에서 도착 지점에 도달하지 못 한 경우 0 리턴
    return 0

for t in range(1,int(input())+1):
    V, E = map(int,input().split())
    # 그래프 입력 받어서 만들기
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int,input().split())
        graph[s] += [e]
    start, end = map(int,input().split())
    # #1 graph = [[], [4, 3], [3, 5], [], [6], [], []]

    # 방문 여부 확인을 위해 선언
    chk = [False]*(V+1)

    sol = bfs(graph,chk,start,end)

    print(f'#{t} {sol}')
