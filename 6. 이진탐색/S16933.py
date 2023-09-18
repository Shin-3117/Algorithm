T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    B = list(map(int,input().split()))
    B.sort()
    sol =0
    for b in B:
        l = 0
        r = N - 1
        
        crossCheck = 0
        while l <= r:
            m = (l+r)//2
            if A[m] == b:
                sol += 1
                break
            elif A[m] > b: # left side
                if crossCheck == 1:
                    break
                r = m-1
                crossCheck = 1
            elif A[m] < b: # right side
                if crossCheck == 2:
                    break
                l = m+1
                crossCheck = 2
    print(f'#{test_case} {sol}')