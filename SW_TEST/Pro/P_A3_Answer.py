def dfs(now):
    global MAP
    global visited
    for next in range(N):
        if MAP[now][next] == 0:
            continue
        if visited[next] == 1:
            continue
        visited[next] = 1
        dfs(next)

def isValid(arr):
    global N 
    global visited 
    
    if len(arr) == 0:
        return False

    visited = [1 for _ in range(N)]
    
    for i in range(len(arr)):
        visited[arr[i]] = 0 
        
    visited[arr[0]] = 1
    dfs(arr[0])
    for i in range(len(arr)):
        if visited[arr[i]] == 0:
            return False
    return True 

def divide(comb):
    global pop 
    
    A = []
    B = [] 
    
    for i in range(N):
        if (comb >> i) & 1:
            A.append(i)
        else:
            B.append(i)
            
    if len(A) == 0 and len(B) == 0:
        return 21e8
    
    if not isValid(A):
        return 21e8
    
    if not isValid(B):
        return 21e8
    
    apop = 0
    bpop = 0
    for i in range(len(A)):
        apop += pop[A[i]]
    for i in range(len(B)):
        bpop += pop[B[i]]
    return abs(apop - bpop)

tc = int(input())
for _ in range(1, tc+1):
    global N
    global MAP
    global pop
    
    N = int(input())
    MAP = [[] for _ in range(N)]
    for i in range(N):
        MAP[i] = list(map(int, input().split()))
    pop = list(map(int, input().split()))
    
    ans = 21e8 
    for i in range(1 << N):
        temp = divide(i)
        if temp < ans:
            ans = temp 
    
    if ans == 21e8:
        ans = 0
    print(f"#{_} {ans}")