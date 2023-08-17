"""
(1 ≤ M ≤ N ≤ 8)
중복이 가능한 경우 : N^N, N=8 까지 가능
8^8 = 1677,7216
"""

import sys
# sys.stdin = open('./inputs/B_15649.txt','r')
N,M = map(int, sys.stdin.readline().split())

s = []

def back():
    # 선택해야 하는 수(M) 만큼 선택 후, 리턴
    if len(s) == M:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,N+1):
        if i not in s:
            s.append(i)
            back()
            s.pop()
back()
"""
만약 n=4, m=2라면 밑과 같은 형태로 진행될 것이다.

s : [1] -> [1,2] -> [1] -> [1,3] -> [1] -> [1,4]

           출력 -> pop(2)  출력 -> pop(3)  출력
"""