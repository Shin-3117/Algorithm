import pprint
T = int(input())
squares = []
N = 0
for i in range(T):
    squares.append(list(map(int,input().split()))) 
    square = squares[i]
    N = max(N,square[0]+square[2],square[1]+square[3])


G = [[0]*N for _ in range(N)]
for k in range(T):
    square = squares[k]
    for i in range(square[0],square[0]+square[2]):
        for j in range(square[1],square[1]+square[3]):
            G[i][j] = k+1
# pprint.pprint(G)
for k in range(T):
    sol = 0
    for i in range(N):
        for j in range(N):
            if G[i][j] == k+1: sol+=1
    print(sol)
# 42
# 53