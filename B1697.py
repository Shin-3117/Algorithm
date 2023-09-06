"""
timeout:2s
N(0 ≤ N ≤ 100,000) K(0 ≤ K ≤ 100,000)
걍 리스트로 해보기
[float('inf')]*100001

"""
from collections import deque
field = [float('inf')]*100001
N,K = map(int, input().split())
move_cnt=0
while field[K]==float('inf'):
    move_cnt+=1
    if 0<N<=100001:
        field[N-1] = min(move_cnt,field[N-1])
    if 0<=N<100001:
        field[N+1] = min(move_cnt,field[N+1])
    field[N*2] = min(move_cnt,field[N*2])
print(field[K])