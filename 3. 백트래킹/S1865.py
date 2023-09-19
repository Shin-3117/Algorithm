import sys
sys.stdin = open('./inputs2/S1865.txt','r')

def DFS(person, percentage):
    global MAX
    if person == N-1:
        MAX = max(percentage, MAX)
        return
    if percentage < MAX or percentage == 0:
        return

    for work in range(N):
        if done[work] == 0:
            done[work] = 1
            DFS(person+1, percentage * P[person+1][work]/100)
            done[work] = 0


T = int(input())
for test in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]

    done = [0] * N # 열은 일의 번호를 의미하고, 이미 한 일은 하지 않는다.
    MAX = 0
    DFS(-1, 1)
    print(f'#{test} {MAX * 100:0.6f}')


# def backTracking(i,j,s):
#     global sol
#     # print(sol,s, i, N)
#     if i == N:
#         if sol < s : 
#             sol = s
#             return

#     for k in range(N):
#         if visited[k] == 0:
#             visited[k] = 1
#             if works[i][k] ==0: continue
#             s *= works[i][k]
#             backTracking(i+1,k,s)
#             s /= works[i][k]
#             visited[k] = 0

# for t in range(int(input())):
#     # 직원 수
#     N = int(input())
#     # 직원이 일에 성공할 확률들
#     works = [list(map(lambda x : float(x)/100,input().split())) for _ in range(N)]
#     # print(works)
#     visited = [0]*N
#     sol=0
#     for j in range(N):
#         if works[0][j] !=0:
#             visited[j] = 1
#             backTracking(1,j,works[0][j])
#             visited[j] = 0
#     sol = float(sol)
#     sol = round(sol*100,6)
#     print(f'#{t+1} {sol:6f}')