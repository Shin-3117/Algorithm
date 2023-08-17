# https://www.acmicpc.net/problem/10163

T = int(input())
squares = []
N = 1001
G = [[0]*N for _ in range(N)]
for k in range(T):
    # squares.append(list(map(int,input().split()))) 
    x0,y0,dx,dy = map(int,input().split())

    # N = max(N,square[0]+square[2],square[1]+square[3])
    for i in range(x0,x0+dx):
        for j in range(y0,dy+y0):
            G[i][j] = k+1

sol = [0]*T
for i in G:
    for j in range(T):
        sol[j]+=i.count(j+1)
for i in sol:
    print(i)
    # for k in range(T):
#     square = squares[k]
#     for i in range(square[0],square[0]+square[2]):
#         for j in range(square[1],square[1]+square[3]):
#             G[i][j] = k+1
# pprint.pprint(G)
# for k in range(T):
#     sol = 0
#     for i in range(N):
#         for j in range(N):
#             if G[i][j] == k+1: sol+=1
#     print(sol)
# 42
# 53
"""
grid = [[0 for _ in range(1001)] for _ in range(1001)]
num_of_papers = int(input())

for p in range(1, num_of_papers+1):
    p_x, p_y, width, height = map(int, input().split())
    for y in range(p_y, p_y+height):
        grid[y][p_x:(p_x+width)] = [p]*width
            
for p in range(1, num_of_papers+1):
    result = 0
    for cnt in range(1001):
        result += grid[cnt].count(p)
    print(result)
"""
