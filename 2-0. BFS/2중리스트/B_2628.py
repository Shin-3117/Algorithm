J,I = map(int,input().split())
total_cut = int(input())
cut_lst = [list(map(int,input().split())) for _ in range(total_cut)]
cut_lst.sort()

cut_i=0
cil=[]
cut_j=0
cjl=[]

for cut in cut_lst:
    if cut[0] == 0: 
        cut_i+=1
        cil.append(cut[1]+cut_i-1)
    elif cut[0] == 1: 
        cut_j+=1
        cjl.append(cut[1]+cut_j-1)
# 자를 만큼 커진 도화지
G = [[1]*(J+cut_j) for _ in range(I+cut_i)]
# 자르기
for i in cil:
    for j in range(J+cut_j):
        G[i][j] = 0
for j in cjl:
    for i in range(I+cut_i):
        G[i][j] = 0


def bfs(i,j):
    di,dj=[1,-1,0,0],[0,0,1,-1]
    q=[]
    q.append([i,j])
    G[i][j] = 0
    cnt = 1
    while q:
        i0,j0 = q.pop(0)
        for move in range(4):
            ii = i0+di[move]
            jj = j0+dj[move]
            if 0<=ii<I+cut_i and 0<=jj<J+cut_j and G[ii][jj] ==1:
                cnt+=1
                q.append([ii,jj])
                G[ii][jj] = 0
    return cnt

sol = 0
for i in range(I+cut_i):
    for j in range(J+cut_j):
        if G[i][j] ==1:
            sol = max(sol,bfs(i,j))
print(sol)