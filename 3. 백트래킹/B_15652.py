"""
(1 ≤ M ≤ N ≤ 8)
중복이 가능한 경우 : N^N, N=8 까지 가능
8^8 = 1677,7216
"""
# 중복가능 조합
import sys
N,M = map(int, sys.stdin.readline().split())

s = []

def back(start):
    if len(s) == M:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,N+1):
        s.append(i)
        back(i)
        s.pop()

back(1)