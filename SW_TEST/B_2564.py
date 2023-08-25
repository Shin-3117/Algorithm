import sys
import pprint
sys.stdin = open('./inputs/B_2564.txt','r')

J,I = map(int,input().split())
G = [[0]*(J+1) for _ in range(I+1)]

N = int(input())
min_d = [float('inf')]*(N+1)
# a: 1은 블록의 북쪽, 2는 블록의 남쪽, 3은 블록의 서쪽, 4는 블록의 동쪽
cnt = 0
for i in range(N):
    cnt+=1
    a, b = map(int,input().split())
    if a == 1:
        G[0][b] = cnt
    elif a == 2:
        G[I][b] = cnt
    elif a == 3:
        G[b][0] = cnt
    elif a == 4:
        G[b][J] = cnt
# x위치
x0, x1 = map(int,input().split())
if x0 == 1:
    G[0][x1] = 'x'
elif x0 == 2:
    G[I][x1] = 'x'
elif x0 == 3:
    G[x1][0] = 'x'
elif x0 == 4:
    G[x1][J] = 'x'

pprint.pprint(G)

def clockMove(i0,j0):
    cnt = 0
    if i0 == 0 and j0!=J:
        for j in range(j0+1,J+1):
            cnt+=1
            if G[0][j] != 0:
                if min_d[G[0][j]] >G[0][j]:
                    min_d[G[0][j]] = cnt
        i0 =0
        j0 =J
