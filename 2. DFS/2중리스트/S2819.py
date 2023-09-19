import sys
sys.stdin = open('./inputs2/S2819.txt','r')
"""
시간복잡도 O는
DFS 사용 : O(V+E) = O(5V) = 80
E=4V, V=4*4

이중 for문 : 4*4 = 16
test cast = 10

80*16*10 = time in
"""
move = [[-1,0], [0,1], [1,0], [0,-1]]

def dfs(i,j,save,cnt):
    save += str(G[i][j])
    cnt += 1

    if cnt ==7:
        lst.add(save)
        return

    for k in move:
        ii = i + k[0]
        jj = j + k[1]
        if 0<=ii<4 and 0<=jj<4:
            dfs(ii,jj,save,cnt)
    

for t in range(int(input())):
    G = [list(map(int,input().split())) for _ in range(4)]
    lst = set()
    for i in range(4):
        for j in range(4):
            dfs(i,j,'',0)
    sol = len(lst)
    # print(lst)
    print(f'#{t+1} {sol}')