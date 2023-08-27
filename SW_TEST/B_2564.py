import sys
import pprint
sys.stdin = open('./inputs/B_2564.txt','r')

J,I = map(int,input().split())
G = [[0]*(J+1) for _ in range(I+1)]

N = int(input())
min_d = [float('inf')]*(N+1)
# a: 1은 블록의 북쪽, 2는 블록의 남쪽, 3은 블록의 서쪽, 4는 블록의 동쪽
cnt = 0
lst = []
for i in range(N):
    cnt+=1
    a, b = map(int,input().split())
    if a == 1:
        G[0][b] = cnt
        lst.append([0,b])
    elif a == 2:
        G[I][b] = cnt
        lst.append([I,b])
    elif a == 3:
        G[b][0] = cnt
        lst.append([b,0])
    elif a == 4:
        G[b][J] = cnt
        lst.append([b,J])
# x위치
x0, x1 = map(int,input().split())
x = []
if x0 == 1:
    G[0][x1] = 'x'
    x = [0,x1]
elif x0 == 2:
    G[I][x1] = 'x'
    x = [I,x1]
elif x0 == 3:
    G[x1][0] = 'x'
    x = [x1,0]
elif x0 == 4:
    G[x1][J] = 'x'
    x = [x1,J]
sol = 0
for i in lst:
    if x0 == 1:
        if i[0] != I:
            sol += abs(x[0]-i[0]) + abs(x[1]-i[1])
        else:
            sol += I + min(x[1]+i[1],2*J-(x[1]+i[1]))
    elif x0 == 2:
        if i[0] != 0:
            sol += abs(x[0]-i[0]) + abs(x[1]-i[1])
        else:
            sol += I + min(x[1]+i[1],2*J-(x[1]+i[1]))
    elif x0 == 3:
        if i[1] != J:
            sol += abs(x[0]-i[0]) + abs(x[1]-i[1])
        else:
            sol += J + min(x[0]+i[0],2*I-(x[0]+i[0]))
    elif x0 == 4:
        if i[1] != 0:
            sol += abs(x[0]-i[0]) + abs(x[1]-i[1])
        else:
            sol += J + min(x[0]+i[0],2*I-(x[0]+i[0]))

print(sol)
# pprint.pprint(G)

# dci = [1,0,-1,0]
# dcj = [0,1,0,-1]
# def clockMove(i0,j0):
#     cnt = 0
#     if i0 == 0 and j0!=J:
#         for j in range(j0+1,J+1):
#             cnt+=1
#             if G[0][j] != 0:
#                 if min_d[G[0][j]] >G[0][j]:
#                     min_d[G[0][j]] = cnt
#         i0 =0
#         j0 =J
