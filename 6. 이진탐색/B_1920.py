"""
N개의 수 정렬 : O(N*logN)
M개의 수 이진탐색 : O(M*logN)
O((N+M)logN) = 2e5 * 30 = 4e6 <10^8
"""
import sys
sys.stdin = open('./inputs/B_1920.txt','r')
input = sys.stdin.readline
N = int(input())
n_lst = list(map(int,input().split()))
M = int(input())
m_lst = list(map(int,input().split()))

n_lst.sort()

def search(s,e,t):
    if s == e :
        print(0)
        return

    mid = (s+e)//2
    if n_lst[mid] == t:
        print(1)
        return
    elif n_lst[mid] < t:
        search(mid+1,e,t)
    else:
        search(s,mid,t)
for i in m_lst:
    search(0,len(n_lst), i)
# time out
# for m in m_lst:
#     if m in n_lst:
#         print(1)
#     else: print(0)