import sys
sys.stdin = open('./inputs2/S5247.txt','r')
"""
!!! pop 안하고 푸는 방법임 !!!
nq =[]
for v, s in q: 조건에 따라 nq에 넣음
q = nq

!!! 혹은 stack 2개 사용해서 que 구현 ~~~

1000001인 lst 생성 후,
BFS를 통해 연산에 따른 값으로 수정
O:V+E = 5V = 5백만
테스트케이스가 10개 이므로
총 O는 5천만 < 1s

"""
# calculations = [('+',1),('-',1),('*',2),('-',10)]

def bfs(N,M):
    G=[]
    L=0
    if M*2<1000000:
        G=[0]*(M*2+1)
        L=M*2+1
    else:
        G=[0]*(M+1)
        L=M+1

    q = [(N,0)]
    while q:
        nq =[]
        for v, s in q:
            if v == M:
                return s

            if v >L or v < 1 or G[v]==1:
                continue

            G[v] = 1
            nq.append((v+1,s+1))
            nq.append((v*2,s+1))
            nq.append((v-1,s+1))
            nq.append((v-10,s+1))
        q = nq

for t in range(int(input())):
    N,M=map(int,input().split())
    sol = bfs(N,M)
    print(f'#{t+1} {sol}')

# while N != M:
    #     sol +=1
    #     if N < M:
    #         # 1000000 연산 중간 결과도 백만 이하 자연수
    #         if 0<N*2<=1000000:
    #             if M-(N+1) < abs(M-(N*2)):
    #                 N += 1
    #             else:
    #                 N *= 2
    #         else: N += 1

    #     elif N > M:
    #         # 1000000 연산 중간 결과도 백만 이하 자연수
    #         if 0<(N-10)<=1000000:
    #             if (N-1)-M < abs((N-10)-M):
    #                 N -= 1
    #             else:
    #                 N -= 10
    #         else: N -= 1