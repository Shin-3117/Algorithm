import sys
sys.stdin = open('./inputs2/S7465.txt','r')
"""2s
BFS O(V+E) : V=100 E=5000 5100
N, M(1 ≤ N ≤ 100, 0 ≤ M ≤ N(N-1)/2)
"""
def bfs(v):
    q=[v]
    cq=[]
    while q:
        for _ in range(len(q)-1):
            cq.append(q.pop())
        v = q.pop()
        q = cq
        cq = []

        visited[v] = 1

        for nv in Vs[v]:
            if visited[nv]==0:
                visited[nv] =1
                q.append(nv)


T=int(input())
for tc in range(1,T+1):
    Vnum, Enum = map(int,input().split())
    Vs = [[] for _ in range(Vnum)]
    visited = [0]*Vnum
    for _ in range(Enum):
        Vstart, Vend = map(int,input().split())
        Vs[Vstart-1].append(Vend-1)
        Vs[Vend-1].append(Vstart-1)
    
    sol = 0
    for i in range(Vnum):
        if visited[i] == 0:
            bfs(i)
            sol +=1

    print(f'#{tc} {sol}')