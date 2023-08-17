"""
(1 ≤ M ≤ N ≤ 8)
중복이 가능한 경우 : N^N, N=8 까지 가능
8^8 = 1677,7216
"""
# 중복 가능 순열
import sys
N,M = map(int, sys.stdin.readline().split())

s = []

def back():
    # 선택해야 하는 수(M) 만큼 선택 후, 리턴
    if len(s) == M:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,N+1):
        s.append(i)
        back()
        s.pop()
back()
