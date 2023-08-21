
import sys
sys.stdin = open('./inputs/S_16658.txt','r')

for t in range(int(input())):
    E, N = map(int,input().split())
    data = list(map(int,input().split()))
    G = [[] for _ in range(1002)]
    for i in range(E):
        G[data[2*i]].append(data[2*i+1])

    sol = 1
    q = [N]
    c = [N]
    while q:
        vs = q.pop(0)
        for v in G[vs]:
            if not v in c:
                sol += 1
                q.append(v)
                c.append(v)

    print(f'#{t+1} {sol}')