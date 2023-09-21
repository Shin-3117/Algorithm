import sys
sys.stdin = open('./inputs2/S5248.txt','r')

for t in range(int(input())):
    N, M = map(int,input().split())
    lst = list(map(int,input().split()))
    V = [[] for _ in range(N+1)]
    for idx in range(M):
        V[lst[2*idx]].append(lst[2*idx+1])
        V[lst[2*idx+1]].append(lst[2*idx])
    # print(V)
    visited = [0]*(N+1)
    cnt = 0
    for idx in range(1,N+1):
        if visited[idx] != 0 : continue
        cnt +=1
        q = []
        q.append(idx)
        while q:
            v = q.pop(0)
            visited[v] = cnt
            for nv in V[v]:
                if visited[nv] == 0:
                    q.append(nv)

    print(f'#{t+1} {cnt}')