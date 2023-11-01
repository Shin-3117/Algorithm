"""시간 제한 2초
N, M은 500,000 이하의 자연수
dict 구조로 빠르게 찾기
"""
N,M = map(int,input().split())
data ={}
for _ in range(N):
    a=input()
    data[a] = a
# print(data)
sol = []
for _ in range(M):
    b=input()
    try:
        sol.append(data[b])
    except: continue
# print(sol)
print(len(sol))
sol.sort()
for i in sol:
    print(i)