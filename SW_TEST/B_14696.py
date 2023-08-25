"""
N 은 1 이상 1,000 이하
4, 3, 2, 1의 순서대로 주어지지 않을 수 있음에 주의
총 개수는 1 이상 100 이하 (a,b 별개)
2 초
"""
for i in range(int(input())):
    A = list(map(int,input().split()))
    a = []
    for i in range(1,A[0]+1):
        a.append(A[i])
    B = list(map(int,input().split()))
    b = []
    for i in range(1,B[0]+1):
        b.append(B[i])
    
    vs_cnt = min(A[0],B[0])
    a.sort(reverse=True)
    b.sort(reverse=True)
    isDone = False
    for vs in range(vs_cnt):
        if a[vs] > b[vs]: 
            print('A')
            isDone = True
            break
        elif a[vs] < b[vs]: 
            print('B')
            isDone = True
            break
    if isDone: continue
    if A[0] > B[0]:
        print('A')
        continue
    elif A[0] < B[0]:
        print('A')
        continue
    elif A[0] == B[0]:
        print('D')
        continue