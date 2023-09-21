# Contact
# dict로 만드는 게 더 느린거 같음
# 규모가 어느 정도 차이나야 더 빠를지 test?
import sys
sys.stdin = open('./inputs/S_1238.txt','r')

def bfs(s):
    q=[s]
    C[s] = -1
    cnt = 0
    while q:
        cnt += 1
        for _ in range(len(q)):
            v = q.pop(0) # 2 / 
            for i in G[v]:
                if C[i] == 0:
                    C[i] = cnt
                    q.append(i)

for t in range(1,2):
    N, S = map(int,input().split())
    # G = [[] for _ in range(101)]
    # C = [0]*101
    G={}
    C={}
    data = list(map(int,input().split()))    
    for i in range(N//2):
        # G[data[i*2]].append(data[i*2+1])
        G.setdefault(data[i*2],[])
        G.setdefault(data[i*2+1],[])
        G[data[i*2]].append(data[i*2+1]) 
        C.setdefault(data[i*2],0)
        C.setdefault(data[i*2+1],0)
    
    print(G)
    print(C)
    bfs(S)
    print(C)
    # top = max(C)
    # for i in range(100,0,-1):
    #     if C[i] == top:
    #         sol = i
    #         break
    tmp = [k for k,v in C.items() if max(C.values()) == v]
    print(tmp)
    sol = max(tmp)
    print(f'#{t} {sol}')