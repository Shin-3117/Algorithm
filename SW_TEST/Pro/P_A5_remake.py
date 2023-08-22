import sys
sys.stdin = open('./SW_TEST/P_A5.txt','r')

input = sys.stdin.readline
#j가 홀수 일때 이동가능 경로 시계방향
di1 = [-1,0,1,1,1,0]
dj1 = [0,1,1,0,-1,-1]
#j가 짝수 일때 이동가능 경로 시계방향
di0 = [-1,-1,0,1,0,-1]
dj0 = [0,1,1,0,-1,-1]

def dfs(i,j,rs,m):
    global sol, C
    if m >= 4:
        sol = max(sol,rs)
        return
    
    for k in range(6):
        if j%2 ==0:
            ii = i + di0[k]
            jj = j + dj0[k]
        else:
            ii = i + di1[k]
            jj = j + dj1[k]

        if 0<=ii<I and 0<=jj<J and C[ii][jj] == False:
            C[ii][jj] = True
            dfs(ii,jj,rs+G[ii][jj],m+1)
            C[ii][jj] = False

def etc(row, col):
    com = [
        [0,4,2],
        [5,1,3]
    ]
    ret = -1
    for i in range(2):
        sum = G[row][col]
        for j in range(3):
            if col%2 ==0:
                nr = row + di0[com[i][j]]
                nc = col + dj0[com[i][j]]
            else:
                nr = row + di1[com[i][j]]
                nc = col + dj1[com[i][j]]
            # nr = row + dr[col % 2][com[i][j]]
            # nc = col + dc[col % 2][com[i][j]]
            if nr < 0 or nr >= I or nc < 0 or nc >= J :
                sum = 0
                break
            sum += G[nr][nc]
        ret = max(sum, ret)
    return ret

# def Ring1(i,j):
#     lst =[]
#     for k in range(6):
#         if j%2 ==0:
#             ii = i + di0[k]
#             jj = j + dj0[k]
#         else:
#             ii = i + di1[k]
#             jj = j + dj1[k]
#         if 0<=ii<I and 0<=jj<J: # and C[ii][jj] == False
#             lst.append(G[ii][jj])
#         else: break
#     if len(lst) >= 3:
#         lst.sort(reverse=True)
#         return lst[0]+lst[1]+lst[2]+G[i][j]
#     else: return 0

# def Ring2(i,j):
#     rs1 = 0
#     C[i][j] = True
#     for k in range(6):
#         # 머리지정
#         rs = G[i][j]
#         if j%2 ==0:
#             ii = i + di0[k]
#             jj = j + dj0[k]
#         else:
#             ii = i + di1[k]
#             jj = j + dj1[k]

#         if 0<=ii<I and 0<=jj<J and C[ii][jj] == False: 
#             C[ii][jj] = True
#             rs += G[ii][jj]
            
#             #꼬리1
#             for k1 in range(6):
#                 if j%2 ==0:
#                     ii1 = i + di0[k1]
#                     jj1 = j + dj0[k1]
#                 else:
#                     ii1 = i + di1[k1]
#                     jj1 = j + dj1[k1]
#                 if 0<=ii1<I and 0<=jj1<J and C[ii1][jj1] == False:
#                     rs += G[ii1][jj1]
#                     C[ii1][jj1] = True
#                     #꼬리2
#                     for k2 in range(6):
#                         if jj1%2 ==0:
#                             ii2 = ii1 + di0[k2]
#                             jj2 = jj1 + dj0[k2]
#                         else:
#                             ii2 = ii1 + di1[k2]
#                             jj2 = jj1 + dj1[k2]
#                         if 0<=ii2<I and 0<=jj2<J and C[ii2][jj2] == False:
#                             rs += G[ii2][jj2]
#                             if rs1 < rs: rs1 =rs
#                             rs -= G[ii2][jj2]
                    
#                     rs -= G[ii1][jj1]
#                     C[ii1][jj1] = False
#             # 머리 초기화
#             rs -= G[ii][jj]
#             C[ii][jj] = False

#     C[i][j] = False
#     return rs1

for t in range(int(input())):
    I,J = map(int,input().split())
    G = [list(map(int,input().split())) for _ in range(I)]
    C = [[False]*J for _ in range(I)]

    sol = 0
    
    for i in range(I):
        for j in range(J):
            C[i][j] = True
            dfs(i,j,G[i][j],1)
            C[i][j] = False
            sol = max(sol,etc(i,j))
            # sol = max(sol,Ring1(i,j),Ring2(i,j))
            # C[i][j] = True
    print(f'#{t+1} {sol}')
