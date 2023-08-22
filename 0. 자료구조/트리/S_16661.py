# 16661. 이진 힙
import sys
sys.stdin = open('./inputs/S_16661.txt','r')

for tc in range(int(input())):
    N = int(input())
    data = [0]
    data.extend(list(map(int,input().split())))
    for idx in range(1,N+1):
        parents = idx//2
        while parents!=0:
            if data[idx] < data[parents]:
                cnt = data[parents]
                data[parents] = data[idx]
                data[idx] = cnt
            parents = parents//2
            idx = idx//2
    
    sol = 0
    while N !=0:
        N = N//2
        sol += data[N]
        
    print(f'#{tc+1} {sol}')