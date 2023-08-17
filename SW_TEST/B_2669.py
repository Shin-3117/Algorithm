# import pprint
squares = [list(map(int,input().split())) for _ in range(4)]

N = 0
for square in squares:
    if max(square) > N:
        N = max(square)
G = [[0]*N for _ in range(N)]
for square in squares:
    for i in range(square[0],square[2]):
        for j in range(square[1],square[3]):
            G[i][j] +=1
sol = 0
for i in range(N):
    for j in range(N):
        if G[i][j] >=1: sol+=1
print(sol)