import sys
sys.stdin = open('./inputs/B_2578.txt','r')

G = [list(map(int,input().split())) for _ in range(5)]
calls = []
for i in range(5):
    calls.extend(list(map(int,input().split())))
# print(calls)

# 입력받은 숫자를 그래프에서 찾아 0으로 만듬
def findNum(INT):
    for i in range(5):
        for j in range(5):
            if G[i][j] == INT:
                G[i][j]=0

def isBingo():
    cnt = 0
    # 줄 빙고 확인
    for i in range(5):
        ci=0
        cj=0
        for j in range(5):
            if G[i][j] == 0: ci+=1
            if G[j][i] == 0: cj+=1
        if ci == 5:cnt+=1
        if cj == 5:cnt+=1
        # if cnt == 3: break
    # 대각선 빙고 확인
    cross1=0
    cross2=0
    for idx in range(5):
        if G[idx][idx] == 0: cross1+=1
        if G[idx][-idx-1] == 0: cross2+=1
    if cross1 == 5:cnt+=1
    if cross2 == 5:cnt+=1

    if cnt >=3:
        return True

#순서대로 숫자 부르기
sol = 0
for call in calls:
    sol += 1
    findNum(call)
    # print(G)
    if isBingo(): break
print(sol)