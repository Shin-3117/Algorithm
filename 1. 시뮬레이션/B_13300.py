"""
학생 수 N(1 ≤ N ≤ 1,000)
한방에 최대 인원 K(1 < K ≤ 1,000)
성별 S(0 or 1)
학년 Y(1 ≤ Y ≤ 6)
"""
N, K = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
data.sort()
# print(data)
S = 7
Y = 7
sol = 0
cnt = 0
while data:
    student = data.pop()
    # 이전 학생과 성별, 학년이 다른 경우
    if student[0] != S or student[1] != Y:
        sol +=1
        cnt = K -1
        S = student[0]
        Y = student[1]
    # 이전 학생과 성별, 학년이 같은 경우
    elif student[0] == S and student[1] == Y:
        cnt -= 1
        if cnt < 0 :
            sol += 1
            cnt = K-1

print(sol)