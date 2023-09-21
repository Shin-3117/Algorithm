# SWEA 노드의 거리
import sys
sys.stdin = open('./inputs/S_16655.txt','r')
# from collections import deque
def bfs(s,e):
    q = []
    # q = deque()
    q.append(s)
    C[s] = 1
    cnt = 0
    while q:
        v = q.pop(0)
        # v = q.popleft()
        for i in G[v]:
            if C[i] == 0:
                C[i] = C[v] + 1
                # if i == e:
                #     return cnt
                q.append(i)
    return C[e]

for t in range(int(input())):
    V, E = map(int,input().split())
    G = [[] for _ in range(V+1)]

    C = [0]*(V+1)
    for _ in range(E):
        a, b = map(int,input().split())
        G[a].append(b)
        G[b].append(a)
    start, end = map(int,input().split())

    sol = bfs(end,start)-1
    if sol < 0 : sol = 0
    print(f"#{t+1} {sol}")