import sys
sys.stdin = open('./inputs2/S2105.txt','r')

moves = [(1,1),(1,-1),(-1,-1),(-1,1)]

def dfs():
    ans = -1                             
    for n in range(N-1, 0, -1): # 큰 마름모 부터 시작 
        for x in range(1, n): # x는 마름모 우하, 좌상 길이 
            y = n-x           # y는 마름모 좌하, 우상 길이
            for si in range(N-n):                         
                for sj in range(y, N-x):        
                    i, j = si, sj
                    desert_list = []            
                    d = 0
                    for _ in range(2 * n):
                        if G[i][j] in desert_list:    
                            break
                        else:
                            desert_list.append(G[i][j])  
                            if i == si+n or j in [sj-y, sj+x]:
                                d += 1
                            i, j = i + moves[d][0], j + moves[d][1] # 이동
                    else:                           
                        ans = 2 * n                 
                        return ans


# 파이썬 15초 50tc
T= int(input())
for tc in range(T):
    N = int(input())
    G = [list(map(int, input().split())) for _ in range(N)]
    
    sol = dfs()
    if sol == None: sol=-1
    print(f'#{tc+1} {sol}')