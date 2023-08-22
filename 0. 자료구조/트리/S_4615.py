# 4615. 재미있는 오셀로 게임
import sys
sys.stdin = open('./inputs/S_4615.txt','r')
# 아래 위 좌 우 # 우하 좌하 상좌 상우
di = [-1,1,0,0, 1,1,-1,-1]
dj = [0,0,-1,1, 1,-1,-1,1]

def bw(i, j, c):
    lst = []
    # 뒤집힐 돌 찾기
    for k in range(8):
        ii = i + di[k]
        jj = j + dj[k]
        while True:
            if table[ii][jj] == c :
                lst.append([ii,jj])
                break
            elif table[ii][jj] == 0 :
                break
            ii += di[k]
            jj += dj[k]
            
    # 뒤집기
    for ij in lst:
        if i<ij[0] and j == ij[1]:
            for idx in range(i,ij[0]):
                table[idx][j] = c
        elif i>ij[0] and j == ij[1]:
            for idx in range(ij[0],i):
                table[idx][j] = c
        elif j<ij[1] and i == ij[0]:
            for idx in range(j,ij[1]):
                table[i][idx] = c
        elif j>ij[1] and i == ij[0]:
            for idx in range(ij[1],j):
                table[i][idx] = c

        elif i<ij[0] and j<ij[1]:
            for idx in range(ij[0] - i):
                table[i+idx][j+idx] = c
        elif i<ij[0] and j>ij[1]:
            for idx in range(ij[0] - i):
                table[i+idx][j-idx] = c
        elif i>ij[0] and j<ij[1]:
            for idx in range(i - ij[0]):
                table[i-idx][j+idx] = c
        elif i>ij[0] and j>ij[1]:
            for idx in range(i - ij[0]):
                table[i-idx][j-idx] = c

for t in range(int(input())):
    N, M = map(int,input().split()) 
    black = 0 # 1
    white = 0 # 2
    table = [[0]*(N+2) for _ in range(N+2)]
    table[N//2][N//2] = 2
    table[N//2+1][N//2+1] = 2
    table[N//2+1][N//2] = 1
    table[N//2][N//2+1] = 1

    for _ in range(M):
        x,y,color = map(int, input().split())
        table[x][y] = color
        bw(x,y,color)
    
    for i in range(1,N+1):
        black += table[i].count(1)
        white += table[i].count(2)
    print(f'#{t+1} {black} {white}')