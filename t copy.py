import sys
import pprint
sys.stdin = open('./inputs/B_13460.txt','r', encoding='utf-8')
input = sys.stdin.readline
I,J = map(int,input().split())
G = [list(input().strip()) for _ in range(I)]
di, dj = [-1,0,1,0], [0,1,0,-1]

sol = 0
O_i,O_j = 0,0
for i in range(I):
    for j in range(J):
        if G[i][j] == 'O':



print(sol)

pprint.pprint(G)