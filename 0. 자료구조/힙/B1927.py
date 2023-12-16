from heapq import heappush, heappop
import sys
sys.stdin = open('./inputs3/B1927.txt','r')
input = sys.stdin.readline

heap = []
for _ in range(int(input())):
    num = int(input())
    # print('a',heap)
    if num == 0:
        try:
            print(heappop(heap))
        except:
            print(0)
    else:
        heappush(heap, num)