T = int(input())

A = list(range(1,13))
n = len(A)
for test_case in range(1, T+1):
    N, K = map(int,input().split())
    sol = 0

    # 주어진 배열 A에 대한 모든 부분집합 생성
    for i in range(1<<n):
    # 1<<len(A) : 1*(2^(배열A의 크기)) = 배열 A의 모든 부분집합의 개수
    # [0, 0] => [0,0] [0,1] [1,0] [1,1] 2^2 
        subset_lst = [] # 부분집합을 저장할 리스트
        for j in range(n): # 원소의 수만큼 비트를 비교
            if i & (1<<j): # i의 j번째 비트가 1인지 아닌지 검사
                subset_lst.append(A[j]) # j번 원소 리스트에 저장
        # 저장이 완료된 리스트의 길이와 합이 일치하면 sol +1
        if len(subset_lst) == N:
            if sum(subset_lst) == K:
                sol += 1
    print(f'#{test_case}', sol)

# https://swexpertacademy.com/main/talk/solvingClub/problemSolverCodeDetail.do

'''input
3
3 6
5 15
5 10
'''