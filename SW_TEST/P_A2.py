import sys
sys.stdin = open('./SW_TEST/P_A2.txt','r')
# DFS + 백트래킹 구현
di,dj =[1,-1,0,0],[0,0,1,-1]

def dfs(move, i,j):
    if move ==3:return
    # 쫄 위치 찾기
    for k in range(4):
        ii = i + di[k]
        jj = j + dj[k]
        # 1(쫄)을 찾을 때까지 ii,jj 증가
        while 0<=ii<N and 0<=jj<N and G[ii][jj] == 0:
            ii += di[k]
            jj += dj[k]
        # 발견 했으면 쫄을 넘어간 상태, 발견을 못 했으면 그래프 나감
        ii += di[k]
        jj += dj[k]

        while 0<=ii<N and 0<=jj<N:
            # 쫄 뒤에 쫄(잡는 경우)
            if G[ii][jj] == 1:
                catch.add((ii,jj))
                G[ii][jj] = 0
                # 잡은 위치에서 다시 탐색
                dfs(move+1,ii,jj)
                # 백트래킹
                G[ii][jj] =1
                # 잡고나서 한칸이동이 불가능
                break
            else:
                # 넘어간 후, 0에서 다시 탐색
                dfs(move+1,ii,jj)
            # while문 진행
            ii += di[k]
            jj += dj[k]

for t in range(int(input())):
    N = int(input())
    G = []
    for i in range(N):
        G.append(list(map(int,input().split())))
        for j in range(N):
            if G[i][j] == 2:
                PO_i = i
                PO_j = j
                G[i][j] = 0
    catch =set()
    dfs(0,PO_i,PO_j)
    sol = len(catch)
    print(f'#{t+1} {sol}')
