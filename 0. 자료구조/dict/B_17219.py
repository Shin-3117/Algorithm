import sys
from collections import deque
sys.stdin = open('./inputs2/B_17219.txt','r')
input = sys.stdin.readline

N,M = map(int,input().split())
data = {}
for _ in range(N):
    site, ps = input().split()
    data[site] = ps

for _ in range(M):
    print(data[input().strip()])

"""
100,000 * 100,000
100,0000,0000
"""