# 5249. 최소 신장 트리
import sys
sys.stdin = open('./inputs2/S5249.txt','r')

import heapq

def dfs(v):
    visited = [0]*(Vnum+1)

    heap = []
    heapq.heappush(heap,(0,v))

    sol = 0
    while heap:
        if sum(visited)==Vnum+1: break
        w, v = heapq.heappop(heap)

        if visited[v] == 0:
            sol += w
            visited[v] =1
            for e in range(Vnum+1):
                if Vs[v][e] !=0 and visited[e] == 0:
                    heapq.heappush(heap,(Vs[v][e],e))
    return sol


for t in range(int(input())):
    Vnum, Enum = map(int,input().split())
    Vs = [[0]*(Vnum+1) for _ in range(Vnum+1)]
    for i in range(Enum):
        n1,n2,w = map(int,input().split())
        Vs[n1][n2] = w
        Vs[n2][n1] = w
    
    sol = dfs(0)
    # for v in range(Vnum+1):
        # dfs_sol = dfs(v)
        # if sol > dfs_sol: sol = dfs_sol

    print(f'#{t+1} {sol}')