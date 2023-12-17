import sys
sys.stdin = open('./inputs3/B2630.txt','r')

N = int(input())
G = [list(map(int,input().split())) for _ in range(N)]
white = 0
blue = 0

def canCut(paperSize,i,j):
    global white, blue
    total = 0
    for pi in range(paperSize):
        for pj in range(paperSize):
            total += G[pi+i][pj+j]
    
    if total == 0: 
        white = white + 1
        # print('add white',paperSize,i,j)
    elif total == paperSize**2:
        blue = blue + 1
        # print('add blue',paperSize,i,j)
    else:
        halfSize = paperSize//2
        if halfSize != 0:
            canCut(halfSize,i,j)
            canCut(halfSize,i+halfSize,j)
            canCut(halfSize,i,j+halfSize)
            canCut(halfSize,i+halfSize,j+halfSize)
canCut(N,0,0)
print(white)
print(blue)