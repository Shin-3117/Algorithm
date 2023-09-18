import sys
sys.stdin = open('inputs2/S1486.txt', 'r')

def BackTracking(n,s):
    global sol
    if s >= B:
        if sol > s-B:
            sol = s-B
        return
    if n == N:
        # global sol
        if s >= B and sol > s-B:
            sol = s-B
        return
    BackTracking(n+1,s+Hs[n])
    BackTracking(n+1,s)

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    Hs = list(map(int, input().split()))
    Hs.sort(reverse=True)
    visited =[0]*N
    sol = float('inf')
    BackTracking(0,0)
    print(f'#{tc} {sol}')