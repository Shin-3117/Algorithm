"""2s
N(1 ≤ N ≤ 100,000)
시작 시간과 끝나는 시간은 2^31-1보다 작거나 같은 자연수 또는 0

lst -> 정렬
NlogN : 500,000
for : 100,000
500,0000,0000
안됨 
X -> 됨 for문은 곱연산이 아니라 합연산
NlogN : 500,000
NlogN : 500,000
for : 100,000
O = 110,0000

"""
import sys
sys.stdin = open("./inputs2/B1931.txt","r")
N = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

lst.sort(key = lambda x: x[0])
lst.sort(key = lambda x: x[1])

cnt = 1
end = lst[0][1]
for i in range(1,N):
    if lst[i][0] >= end:
        cnt +=1
        end = lst[i][1]
print(cnt)