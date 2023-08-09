# https://www.acmicpc.net/problem/2667
"""
1. Idea
-2중 for and 미방시 -> DFS
- DFS를 통해 찾은 값 저장 후 정렬 후 출력

2. 시간복잡도
DFS : O(V+E) = 5*N^2
V = N^2
E = 4*N^2

3. 자료구조
- 그래프 저장 : int[][]
- 방문 여부 : bool[][]
- 결과값 : int[]
"""
# 의외인점 chk 안 만들고 map 수정하는 거보다 chk 만든게 더 빠름
# 안 만듬 (52ms / 31332KB) chk만듬 (44ms / 31332KB)
import sys
sys.stdin = open('./inputs/B_2667.txt','r', encoding='utf-8')
N = int(sys.stdin.readline())
#! 붙어있는 입력같 분리 방법
#sys.stdin.readline().strip()로 문자열을 받아들이고 int로 순회
map = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]
chk = [[False]*N for _ in range(N)]

sol =[]
each =0
di, dj = [1,0,-1,0], [0,1,0,-1]
def dfs(i,j):
    global each
    each +=1
    for k in range(4):
        ii = i+di[k]
        jj = j+dj[k]
        if 0<=ii<N and 0<=jj<N and chk[ii][jj] == False:
            if map[ii][jj] == 1:
                chk[ii][jj] = True
                dfs(ii,jj)

for i in range(N):
    for j in range(N):
        if map[i][j] ==1 and chk[i][j] == False:
            # 방문 처리
            chk[i][j] =True
            each = 0
            dfs(i,j)
            # DFS로 크기 구하기
            # 크기를 결과 리스트에 넣기
            sol.append(each)
sol.sort()
print(len(sol))
for i in sol:
    print(i)