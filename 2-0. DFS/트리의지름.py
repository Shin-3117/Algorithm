import sys
sys.stdin = open('./inputs3/B1167.txt','r')

V = int(input())
N = [[] for _ in range(V+1)]

for _ in range(V):
    NiList = list(map(int,input().split()))
    Ni = NiList[0]
    for i in range(1,len(NiList)-1,2):
        N[Ni].append((NiList[i],NiList[i+1]))

# print(N)

visited=[0]*(V+1)
sol1 = [0,0]
def dfs(start,total_d):
    visited[start]=1
    for Vi in N[start]:
        v, d = Vi
        if visited[v]==0:
            visited[v]=1
            dfs(v,d+total_d)
        
        if visited[v]==1:
            global sol1
            if sol1[1] < total_d:
                sol1 = [start,total_d]
            # print([start,total_d])
dfs(1,0)
# print(sol1)

start2 = sol1[0]
visited=[0]*(V+1)
# print(0)
dfs(start2,0)
print(sol1[1])