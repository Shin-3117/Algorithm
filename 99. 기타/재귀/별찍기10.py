#https://www.acmicpc.net/problem/2447
# n = 27 혹은 3의 제곱
n = int(input())
G = [['*']*n for _ in range(n)]
def draw(n,I,J):
    if n == 1: return
    n1 = n//3
    for i in range(n1+I,n1*2+I):
        for j in range(n1+J,n1*2+J):
            G[i][j] = ' '
    for i in range(0+I,n+I,n1):
        for j in range(0+J, n+J, n1):
            draw(n1,i,j)
draw(n,0,0)

for i in G:
    print(''.join(i))