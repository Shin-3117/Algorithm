import sys
sys.stdin = open('./inputs/S_16494.txt','r', encoding='utf-8')
sol = 0

def bfs(G, C, S, E):
    global sol
    C[S] = True
    for i in G[S]:
        if i == E: sol = 1
        elif G[i] != [] and C[i] == False:
            bfs(G,C, i, E)

for t in range(1,int(input())+1):
    V, E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int,input().split())
        graph[s] += [e]
    start, end = map(int,input().split())
    chk = [False]*(V+1)

    bfs(graph,chk,start,end)

    print(f'#{t} {sol}')
    sol=0