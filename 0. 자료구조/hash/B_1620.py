import sys
sys.stdin = open('./inputs2/B_1620.txt','r')
input = sys.stdin.readline
n,m = map(int,input().split())
# data=[input().strip() for _ in range(n)]
# for _ in range(m):
#     a = input().strip()
#     try:
#         a = int(a)
#         print(list(data.keys())[a-1])
#     except:
#         print(data[a])
data= {}
for i in range(1,n+1):
    a = input().strip()
    data[a] = i
    data[str(i)] = a
for _ in range(m):
    a = input().strip()
    print(data[a])