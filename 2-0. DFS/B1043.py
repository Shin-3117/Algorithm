import sys
sys.stdin = open('./inputs3/B1043.txt','r')

N, M = map(int,input().split())
knowTrue = input()

if knowTrue == '0':
    print(M)
else:
    Node = [set() for _ in range(N+1)]
    
    knowTrue = list(map(int,knowTrue.split()))
    knowNum = knowTrue.pop(0)
    
    parties = []
    for _ in range(M):
        party = list(map(int,input().split()))
        partyNum = party.pop(0)
        for i in party:
            Node[i].update(party)
        parties.append(party)
    # print(Node)
    # print(parties)

    #아는사람찾기
    totalKnows = set()
    visited = [0]*(N+1)
    # print(visited)
    for i in knowTrue:
        #dfs
        stack = [i]
        while stack:
            n = stack.pop()
            totalKnows.add(n)
            visited[n]=1
            for v in Node[n]:
                if visited[v]==0:
                    stack.append(v)
    # print(totalKnows)

    #거짓말이 가능한 파티 수
    ans = 0
    for party in parties:
        isPossible = True
        for p in party:
            if p in totalKnows:
                isPossible = False
                break
        if isPossible: ans+=1
    print(ans)

