import sys
sys.stdin = open('./inputs/B_1260.txt','r', encoding='utf-8')
V, E, start = map(int,sys.stdin.readline().split())
G =[[] for _ in range(V+1)]
for _ in range(E):
    a,b = map(int,sys.stdin.readline().split())
    G[a] += [b]
    G[b] += [a]
C1 =[False]*(V+1)
C2 =[False]*(V+1)

def dfs(G,C,S):
    C[S] = True
    print(S, end=' ')
    for i in G[S]:
        if not C[i]:
            dfs(G, C, i)

def bfs(G,C,S):
    pass

dfs(G,C1,start)