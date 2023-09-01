Vertex_num,Edge_num,start_node = map(int,input().split())
G = [[] for _ in range(Vertex_num+1)]
for _ in range(Edge_num):
    sv,ev = map(int,input().split())
    G[sv].append(ev)
    G[ev].append(sv)
    G[sv].sort()
    G[ev].sort()
# print(G)
visited = []
dfs_str = ''
def dfs(s):
    global dfs_str
    dfs_str += str(s)+' '
    visited.append(s)
    for i in G[s]:
        if i not in visited:
            visited.append(i)
            dfs(i)

def bfs(s):
    bfs_str = ''
    q=[s]
    C=[s]
    while q:
        v= q.pop(0)
        bfs_str += str(v)+' '
        for i in G[v]:
            if i not in C:
                q.append(i)
                C.append(i)
    return bfs_str

dfs(start_node)
print(dfs_str)
print(bfs(start_node))